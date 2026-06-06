import dsc40graph
from dsf import DisjointSetForest

def slc(graph, d, k):
    '''
    Performs single linkage clustering using Kruskal's algorithm.
    '''
    # TODO: Implement the slc function

    nodes = list(graph.nodes)
    forest = DisjointSetForest(nodes)
    num_clusters = len(nodes)

    # Kruskal: consider edges from smallest distance to largest distance.
    edges = sorted(list(graph.edges), key=d)

    for u, v in edges:
        # Stop as soon as we have exactly k clusters.
        if num_clusters == k:
            break

        # Only merge if this edge connects two different clusters.
        if not forest.in_same_set(u, v):
            forest.union(u, v)
            num_clusters -= 1

    # Group nodes by their current representative.
    clusters = {}
    for node in nodes:
        rep = forest.find_set(node)
        if rep not in clusters:
            clusters[rep] = set()
        clusters[rep].add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())