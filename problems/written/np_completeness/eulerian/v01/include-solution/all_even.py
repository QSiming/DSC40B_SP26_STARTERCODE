def all_degrees_even(graph):
    for node in graph:
        if graph.neighbors(node) % 2 != 0:
            # the degree is odd
            return False
    return True
