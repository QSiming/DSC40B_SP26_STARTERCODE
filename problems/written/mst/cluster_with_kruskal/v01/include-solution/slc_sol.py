import dsc40graph

def slc(graph, d, k):
    components = DisjointSetForest(graph.nodes)
    sorted_edges = sorted(graph.edges, key=d)

    n_edges = 0
    for (u, v) in sorted_edges:
        if n_edges == len(graph.nodes) - k:
            break
        if not components.in_same_set(u, v):
            components.union(u, v)
            n_edges += 1

    # we can infer the cluster memberships from the DSF. we look up each node's cluster
    # representative
    clusters = {}
    for node in graph.nodes:
        cluster_representative = components.find_set(node)
        if cluster_representative not in clusters:
            clusters[cluster_representative] = set()

        clusters[cluster_representative].add(node)

    return frozenset(frozenset(v) for v in clusters.values())
