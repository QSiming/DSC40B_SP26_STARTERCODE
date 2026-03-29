import slc

from autogradescope.decorators import weight

import dsc40graph


DEFAULT_VISIBILITY = 'visible'


@weight(3)
def test_example():
    """Test the example graph given in the writeup."""
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]

    for edge in edges: g.add_edge(*edge)

    def d(edge):
        u, v = sorted(edge)
        return {
            ('a', 'b'): 1,
            ('a', 'c'): 4,
            ('b', 'd'): 3,
            ('c', 'd'): 2,
        }[(u, v)]

    assert slc.slc(g, d, 2) == frozenset([
            frozenset(['a', 'b']),
            frozenset(['c', 'd']),
    ])

@weight(2)
def test_with_one_cluster():
    """Does it work when k = 1?"""
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]

    for edge in edges: g.add_edge(*edge)

    def d(edge):
        u, v = sorted(edge)
        return {
            ('a', 'b'): 1,
            ('a', 'c'): 4,
            ('b', 'd'): 3,
            ('c', 'd'): 2,
        }[(u, v)]

    assert slc.slc(g, d, 1) == frozenset([
            frozenset(['a', 'b', 'c', 'd']),
    ])
