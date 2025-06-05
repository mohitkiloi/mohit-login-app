import pandas as pd
import networkx as nx

# Load login logs
logs = pd.read_csv("/logs.csv")

G = nx.Graph()

for _, row in logs.iterrows():
    user = row['email']
    ip = row['ip']
    device = row['user_agent']

    G.add_edge(user, ip, type='logged_from')
    G.add_edge(user, device, type='used_device')

# Save as edge list
edges = list(G.edges(data=True))
with open("login_graph.csv", "w") as f:
    f.write("source,target,relation\n")
    for u, v, data in edges:
        f.write(f"{u},{v},{data['type']}\n")
