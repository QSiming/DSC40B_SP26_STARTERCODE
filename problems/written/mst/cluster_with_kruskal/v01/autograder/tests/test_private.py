from autogradescope.decorators import weight

import time

import dsc40graph

import slc


DEFAULT_VISIBILITY = 'after_published'

def test_with_each_node_in_own_cluster():
    """Does it work when k = |V|?"""
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

    assert slc.slc(g, d, 4) == frozenset([
            frozenset(['a']),
            frozenset(['b']),
            frozenset(['c']),
            frozenset(['d'])
        ])

def test_correctness_with_large_graph():
    """Does it work on a large complete graph?"""
    g = dsc40graph.UndirectedGraph()
    for i in range(1_000):
        for j in range(i + 1, 1_000):
            g.add_edge(i, j)

    def d(edge):
        u, v = edge
        return u + v

    expected_clusters = slc.slc(g, d, 6)

    # canonicalize the clusters
    expected_clusters = list(sorted(expected_clusters, key=len))

    assert len(expected_clusters) == 6

    assert expected_clusters[0] == frozenset([995])
    assert expected_clusters[1] == frozenset([996])
    assert expected_clusters[2] == frozenset([997])
    assert len(expected_clusters[5]) == 995


def test_efficiency_with_large_graph():
    """Does it run in a reasonable amount of time?"""
    g = dsc40graph.UndirectedGraph()
    for i in range(1_000):
        for j in range(i + 1, 1_000):
            g.add_edge(i, j)

    def d(edge):
        u, v = edge
        return u + v

    start = time.time()
    expected_clusters = slc.slc(g, d, 6)
    stop = time.time()
    elapsed_time = stop - start

    # should take (much) less than 20 seconds; should take around 1 second
    assert elapsed_time < 20



def test_with_float_weights():
    """Does it work when distances are floats?"""
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]

    for edge in edges: g.add_edge(*edge)

    def d(edge):
        u, v = sorted(edge)
        return {
            ('a', 'b'): .1,
            ('a', 'c'): .4,
            ('b', 'd'): .3,
            ('c', 'd'): .2,
        }[(u, v)]

    assert slc.slc(g, d, 3) == frozenset([
            frozenset(['a', 'b']),
            frozenset(['d']),
            frozenset(['c']),
        ])


def test_with_negative_weights():
    """Does it work when distances can be negative?"""
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]

    for edge in edges: g.add_edge(*edge)

    def d(edge):
        u, v = sorted(edge)
        return {
            ('a', 'b'): .1,
            ('a', 'c'): -.4,
            ('b', 'd'): -.3,
            ('c', 'd'): .2,
        }[(u, v)]

    assert slc.slc(g, d, 3) == frozenset([
            frozenset(['a', 'c']),
            frozenset(['b']),
            frozenset(['d']),
        ])
