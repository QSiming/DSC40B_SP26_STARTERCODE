from autogradescope.decorators import weight, visibility
import dsc40graph

# import the student's code
import cluster


DEFAULT_VISIBILITY = 'visible'


@visibility('visible')
@weight(1)
def test_function_on_simple_example():

    graph = dsc40graph.UndirectedGraph()
    for n in ['a', 'b', 'c', 'd']:
        graph.add_node(n)

    for u, v in [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]:
        graph.add_edge(u, v)

    def symmetrize(dct) -> callable:
        """Create a function for accessing unordered edges stored in a dict."""
        def func(u, v):
            if (u, v) in dct:
                return dct[(u, v)]
            else:
                return dct[(v, u)]
        return func

    weights = symmetrize({
            ('a', 'b'): 1,
            ('a', 'd'): .2,
            ('b', 'c'): .3,
            ('c', 'd'): .9,
        })

    your_answer = cluster.cluster(graph, weights, .4)
    expected_output = frozenset([
        frozenset(['a', 'b']),
        frozenset(['c', 'd'])
        ])

    assert your_answer == expected_output
