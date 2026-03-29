def cluster(graph, weights, level):
    status = {node: 'undiscovered' for node in graph.nodes}
    #list to store frozensets
    lst = []
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            # These nodes were visited on one iteration of BFS
            # meaning they are connected
            visited = bfs(graph, node, weights, level, status)
            # append these connected elements
            lst.append(frozenset(visited))
    return frozenset(lst)

def bfs(graph, source, weights, level, status=None):
    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}
    status[source] = 'pending'
    pending = deque([source])
    # create visited array to hold changed elements
    visited = []
    # while there are still pending nodes
    while pending: 
        u = pending.popleft()
        for v in graph.neighbors(u):
            # explore edge (u,v) only if weight is greater than level
            if weights(u,v) < level:
                continue

            if status[v] == 'undiscovered':
                status[v] = 'pending'
                # append to right
                pending.append(v)
        status[u] = 'visited'
        visited.append(u)
    return visited
