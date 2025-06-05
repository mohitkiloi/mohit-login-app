import torch
from torch_geometric.data import Data
from gnn_model import GNN  # import your model
import pandas as pd
import numpy as np

# Load edge list and nodes like before
edge_df = pd.read_csv("login_graph.csv")
nodes = pd.unique(edge_df[['source', 'target']].values.ravel())
node_id_map = {node: i for i, node in enumerate(nodes)}

edge_index = torch.tensor([
    [node_id_map[src] for src in edge_df['source']],
    [node_id_map[tgt] for tgt in edge_df['target']]
], dtype=torch.long)

x = torch.eye(len(nodes), dtype=torch.float)
data = Data(x=x, edge_index=edge_index)

# Load trained model
model = GNN(in_channels=x.shape[1], out_channels=5)  # change based on your #labels
model.load_state_dict(torch.load("gnn_model.pth"))
model.eval()

# Predict
with torch.no_grad():
    logits = model(data)
    predictions = torch.argmax(logits, dim=1)

# Decode labels
from sklearn.preprocessing import LabelEncoder
log_data = pd.read_csv("logs.csv")
le = LabelEncoder()
le.fit(log_data[log_data['attack_type'] != "normal"]['attack_type'])

for i, node in enumerate(nodes):
    print(f"{node} -> {le.inverse_transform([predictions[i].item()])[0]}")


