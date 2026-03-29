import dsc40graph
from collections import deque
import assign_good_and_evil as student
from autogradescope.decorators import weight


def assign_good_and_evil(graph):
    """
    the answer key solution
    """
    label = {}
    status = {node: 'undiscovered' for node in graph.nodes}
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            possible = good_and_evil_bfs(graph, node, status, label)
            if not possible:
                return None

    return label


def good_and_evil_bfs(graph, source, status, label):
    """
    helper function for the answer key solution
    """
    status[source] = 'pending'
    label[source] = 'good'
    pending = deque([source])

    # while there are still pending nodes
    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            # explore edge (u,v)
            if status[v] == 'undiscovered':
                status[v] = 'pending'
                if label[u] == 'good':
                    label[v] = 'evil'
                else:
                    label[v] = 'good'
                # append to right
                pending.append(v)
            elif label[u] == label[v]:
                return False
        status[u] = 'visited'

    return True


def bfs(graph, source, status=None):
    """
    Helper function for full_bfs
    Returns a connected component of schools.
    """

    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}

    status[source] = 'pending'
    pending = deque([source])
    visited_nodes = []
    # while there are still pending nodes
    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            # explore edge (u,v)
            if status[v] == 'undiscovered':
                status[v] = 'pending'
                # append to right
                pending.append(v)
        status[u] = 'visited'
        visited_nodes.append(u)

    return visited_nodes


def full_bfs(graph):
    """
    Performs a full bfs on the graph.
    Returns a list of connect components of schools.
    If A, B, and C are in one component and D is in its own component,
    the output would be [[A, B, C], [D]], unordered.
    """
    connected_components = []
    status = {node: 'undiscovered' for node in graph.nodes}
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            connected_components.append(bfs(graph, node, status))

    return connected_components


def check_answer(example_graph, student_answer, answer):
    """
    Checks whether the student's answer is a viable answer.
    If student is"""

    if answer == None:
        assert student_answer == None
        print('The only valid answer is None')
        return

    connected_components = full_bfs(example_graph)

    # checks the student_answer is a dictionary
    assert isinstance(student_answer, dict)

    # checks whether student's dictionary contains all school names
    assert set(answer.keys()).issubset(student_answer.keys())

    # checks whether student's dictionary contains valid labels
    assert set(student_answer.values()) == set(['good', 'evil'])

    for component in connected_components:
        first_school = component[0]
        answer_label = answer[first_school]  # Justin - Michigan: evil
        # Student - Michigan: good
        student_label = student_answer[first_school]
        match = answer_label == student_label  # match: False

        if match:
            for school in component:
                assert student_answer[school] == answer[school]

        if not match:
            for school in component:
                assert student_answer[school] != answer[school]

    print("A possible dictionary would be:")
    print(answer)


DEFAULT_VISIBILITY = 'visible'


@weight(2)
def test_1():
    """Public test: test case from the homework PDF"""

    rivalry_graph = dsc40graph.UndirectedGraph()
    rivalry_graph.add_edge('Michigan', 'OSU')
    rivalry_graph.add_edge('USC', 'OSU')
    rivalry_graph.add_edge('USC', 'UCLA')
    rivalry_graph.add_node('UCSD')

    answer = assign_good_and_evil(rivalry_graph)
    student_answer = student.assign_good_and_evil(rivalry_graph)
    check_answer(rivalry_graph, student_answer, answer)
