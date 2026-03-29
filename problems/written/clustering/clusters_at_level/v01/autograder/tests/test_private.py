import time

from autogradescope.decorators import weight, visibility
import dsc40graph

# import the student's code
import cluster


DEFAULT_VISIBILITY = 'after_published'


def symmetrize(dct) -> callable:
        """Create a function for accessing unordered edges stored in a dict."""
        def func(u, v):
            if (u, v) in dct:
                return dct[(u, v)]
            else:
                return dct[(v, u)]
        return func


@weight(1)
def test_with_edge_equal_to_level():

    graph = dsc40graph.UndirectedGraph()
    for n in ['a', 'b', 'c', 'd']:
        graph.add_node(n)

    for u, v in [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]:
        graph.add_edge(u, v)

    weights = symmetrize({
            ('a', 'b'): 1,
            ('a', 'd'): .2,
            ('b', 'c'): .3,
            ('c', 'd'): .9,
        })


    your_answer = cluster.cluster(graph, weights, .3)
    expected_output = frozenset([
                    frozenset(['a', 'b', 'c', 'd']),
                ])
    assert your_answer == expected_output

@weight(1)
def test_with_three_clusters():

    graph = dsc40graph.UndirectedGraph()
    for n in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        graph.add_node(n)

    edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd'), ('e', 'f'),
            ('f', 'g') ]

    for u, v in edges:
        graph.add_edge(u, v)

    weights = symmetrize({
            ('a', 'b'): 1,
            ('a', 'd'): .2,
            ('b', 'c'): .3,
            ('c', 'd'): .9,
            ('e', 'f'): .5,
            ('g', 'f'): .7,
        })


    your_answer = cluster.cluster(graph, weights, .4)
    expected_output = frozenset([
                    frozenset(['a', 'b']),
                    frozenset(['c', 'd']),
                    frozenset(['e', 'f', 'g']),
                ])
    assert your_answer == expected_output


@weight(1)
def test_with_high_level_so_each_node_is_a_cluster():

    graph = dsc40graph.UndirectedGraph()
    for n in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        graph.add_node(n)

    edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd'), ('e', 'f'),
            ('f', 'g') ]

    for u, v in edges:
        graph.add_edge(u, v)

    weights = symmetrize({
            ('a', 'b'): .9,
            ('a', 'd'): .2,
            ('b', 'c'): .3,
            ('c', 'd'): .9,
            ('e', 'f'): .5,
            ('g', 'f'): .7,
        })


    your_answer = cluster.cluster(graph, weights, 1)
    expected_output = frozenset([
                    frozenset(['a']),
                    frozenset(['b']),
                    frozenset(['c']),
                    frozenset(['d']),
                    frozenset(['e']),
                    frozenset(['f']),
                    frozenset(['g']),
                ])
    assert your_answer == expected_output

@weight(1)
def test_with_low_level():

    graph = dsc40graph.UndirectedGraph()
    for n in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        graph.add_node(n)

    edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd'), ('e', 'f'),
            ('f', 'g') ]

    for u, v in edges:
        graph.add_edge(u, v)

    weights = symmetrize({
            ('a', 'b'): .9,
            ('a', 'd'): .2,
            ('b', 'c'): .3,
            ('c', 'd'): .9,
            ('e', 'f'): .5,
            ('g', 'f'): .7,
        })


    your_answer = cluster.cluster(graph, weights, .01)
    expected_output = frozenset([
                    frozenset(['a', 'b', 'c', 'd']),
                    frozenset(['e', 'f', 'g']),
                ])
    assert your_answer == expected_output


@weight(2)
def test_time_complexity_empirically():
    """Test time complexity empirically.
    This test times your code on a large input. This test will fail only if your code
    takes much, *much* longer than the reference solution. If this happens, your
    code most likely has the incorrect time complexity.
    """
    # in case someone implements DFS, we need to raise the recursion limit
    import sys
    sys.setrecursionlimit(2_000)

    # make a large complete graph with two clusters
    graph = dsc40graph.UndirectedGraph()
    n = 1_000
    for i in range(n):
        graph.add_node(i)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph.add_edge(i, j)

    def weights(i, j):
        if i <= n // 2 and j <= n // 2:
            return .8
        elif i >= n // 2 and j >= n // 2:
            return .8
        else:
            return .3

    start = time.time()
    your_answer = cluster.cluster(graph, weights, .5)
    finish = time.time()

    elapsed = finish - start
    assert elapsed < 10
