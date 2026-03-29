def cluster(graph, weights, t):
    status = {'undiscovered' for node in graph.nodes}
    clusters = []
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            cluster = bfs_cluster(graph, node, weights, status, t)
            clusters.append(cluster)

def bfs_connected_components_with_threshold(
        graph, source, weights, status, t):
    cluster = [source]
    pending = deque([source])
    status[source] = 'pending'
    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            if status[v] == 'undiscovered' and weight(u, v) <= t:
                pending.append(v)
                status[v] = 'pending'
                cluster.append(v)
    status[u] = 'visited'
    return cluster
