def cluster(graph, weights, level):
    '''
    Clusters a graph based on similarity.
    '''
    # TODO: Implement the cluster function
    visited = set()
    clusters = []

    for start in graph.nodes:
        if start not in visited:
            current_cluster = set()
            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                current_cluster.add(node)

                for neighbor in graph.neighbors(node):
                    if neighbor not in visited and weights(node, neighbor) >= level:
                        visited.add(neighbor)
                        queue.append(neighbor)

            clusters.append(frozenset(current_cluster))

    return frozenset(clusters)
