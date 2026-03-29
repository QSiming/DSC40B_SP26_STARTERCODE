import dsc40graph
from autogradescope.decorators import weight


from biggest_descendent import biggest_descendent


DEFAULT_VISIBILITY = 'visible'


@weight(1)
def test_1():
    """Example from problem statement."""
    graph = dsc40graph.DirectedGraph()
    edges = [(1,2), (2,4), (2,5), (4,8), (4,9), (1,3), (3,6), (3,7)]
    for edge in edges:
        graph.add_edge(*edge)

    values = {
        1: 2,
        2: 1,
        3: 4,
        4: 8,
        5: 5,
        6: 2,
        7: 10,
        8: 3,
        9: 9
    }

    your_result = biggest_descendent(graph, 1, values)
    right_answer = {1: 10, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

    assert your_result == right_answer
