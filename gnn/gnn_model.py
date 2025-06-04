import pandas as pd
import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
import networkx as nx
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load edge list
edge_df = pd.read_csv("login_graph.csv")

# Map each node to a unique integer ID
nodes = pd.unique(edge_df[['source', 'target']].values.ravel())
node_id_map = {node: i for i, node in enumerate(nodes)}

# Convert edges to tensor format
edge_index = torch.tensor([
    [node_id_map[src] for src in edge_df['source']],
    [node_id_map[tgt] for tgt in edge_df['target']]
], dtype=torch.long)

# Dummy node features (can be improved by adding metadata)
x = torch.eye(len(nodes), dtype=torch.float)

# Load labels (attack types) from logs.csv
log_data = pd.read_csv("../logs.csv")
log_data = log_data[log_data['attack_type'] != 'normal']  # filter out normal
log_data = log_data[log_data['email'].isin(node_id_map)]

# Encode labels
label_encoder = LabelEncoder()
log_data['label'] = label_encoder.fit_transform(log_data['attack_type'])

# Create labels for user nodes only
y = torch.full((len(nodes),), -1)
for _, row in log_data.iterrows():
    idx = node_id_map[row['email']]
    y[idx] = row['label']

# Build PyTorch Geometric Data object
data = Data(x=x, edge_index=edge_index, y=y)

# Define GCN model
class GNN(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(in_channels, 32)
        self.conv2 = GCNConv(32, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x

model = GNN(in_channels=x.shape[1], out_channels=len(label_encoder.classes_))
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

# Train the model
model.train()
for epoch in range(100):
    optimizer.zero_grad()
    out = model(data)
    mask = data.y != -1  # Train only on labeled nodes
    loss = criterion(out[mask], data.y[mask])
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Save model
torch.save(model.state_dict(), "gnn_model.pth")
print(" Trained GNN model and saved as gnn_model.pth")
