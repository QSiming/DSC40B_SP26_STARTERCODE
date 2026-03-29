from collections import deque

def cluster(graph, weights, level):
    status = {node: 'undiscovered' for node in graph.nodes}
    components = []
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            component = _bfs_clusterer(graph, node, status, weights, level)
            components.append(component)
    return _freeze(components)


def _bfs_clusterer(graph, source, status, weights, level):
    status[source] = 'pending'
    pending = deque([source])
    component = []

    # while there are still pending nodes
    while pending: 
        u = pending.popleft()
        component.append(u)
        for v in graph.neighbors(u):
            # explore edge (u,v)
            if (weights(u, v) >= level) and (status[v] == 'undiscovered'):
                status[v] = 'pending'
                # append to right
                pending.append(v)
        status[u] = 'visited'

    return component

def _freeze(nested_lists):
    return frozenset(frozenset(lst) for lst in nested_lists)
