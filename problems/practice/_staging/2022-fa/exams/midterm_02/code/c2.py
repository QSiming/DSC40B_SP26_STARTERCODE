def foo(graph, u):
    count = 1
    for v in graph.neighbors(u):
        count += foo(graph, v)
    return count

import dsc40graph
graph = dsc40graph.DirectedGraph()
