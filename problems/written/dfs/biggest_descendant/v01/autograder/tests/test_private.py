from autogradescope.decorators import weight
import time

import dsc40graph

from biggest_descendent import biggest_descendent


DEFAULT_VISIBILITY = 'after_published'

@weight(1)
def test_1():
    """Graph with two nodes."""
    graph = dsc40graph.DirectedGraph()

    edges = [(1,2)]
    for edge in edges:
        graph.add_edge(*edge)

    values = {
        1: 1,
        2: 2
    }

    your_answer = biggest_descendent(graph, 1, values)
    assert your_answer == {1: 2, 2: 2}


@weight(1)
def test_2():
    """Graph with more nodes."""
    graph = dsc40graph.DirectedGraph()

    edges = [(1,2), (2,4), (2,6), (7,8), (4,9), (1,3), (4,6), (3,7)]
    for edge in edges:
        graph.add_edge(*edge)

    values = {
        1: 2,
        2: 1,
        3: 4,
        4: 8,
        6: 2,
        7: 10,
        8: 3,
        9: 9
    }

    your_answer = biggest_descendent(graph, 1, values)
    assert your_answer == {1: 10, 2:9, 3: 10, 4: 9, 6: 2, 7: 10, 8: 3, 9: 9}

@weight(2)
def test_3():
    """Graph with more nodes, another example."""
    graph = dsc40graph.DirectedGraph()

    edges = [(1,2), (2,4), (2,5), (4,8), (4,9), (1,3), (3,6), (3,7)]
    for edge in edges:
        graph.add_edge(*edge)

    values = {
        1: 10,
        2: 9,
        3: 10,
        4: 9,
        5: 5,
        6: 2,
        7: 10,
        8: 3,
        9: 9
    }

    your_answer = biggest_descendent(graph, 1, values)
    assert your_answer == {1: 10, 2: 9, 4: 9, 8: 3, 9: 9, 5: 5, 3: 10, 6: 2, 7: 10}


@weight(2)
def test_5():
    """A very large tree"""
    graph = dsc40graph.DirectedGraph()

    # a large binary tree
    for i in range(10_000):
        graph.add_edge(i, 2*i)
        graph.add_edge(i, 2*i + 1)

    values = {}
    for i, u in enumerate(graph.nodes):
        values[u] = i

    your_answer = biggest_descendent(graph, 1, values)
    assert your_answer[1] == 19_999
    assert your_answer[5] == 12_287
    assert your_answer[150] == 19_327
    assert your_answer[10_000] == 10_000


@weight(1)
def test_efficiency():
    """Check efficiency empirically on a large tree"""
    graph = dsc40graph.DirectedGraph()

    # a large binary tree
    for i in range(10_000):
        graph.add_edge(i, 2*i)
        graph.add_edge(i, 2*i + 1)

    values = {}
    for i, u in enumerate(graph.nodes):
        values[u] = i

    start = time.time()
    your_answer = biggest_descendent(graph, 1, values)
    stop = time.time()

    elapsed_time = stop - start
    assert elapsed_time < 60
