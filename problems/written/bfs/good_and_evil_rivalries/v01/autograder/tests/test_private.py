import assign_good_and_evil as student

from autogradescope.decorators import weight
import dsc40graph
import time
from test_public import assign_good_and_evil, check_answer

DEFAULT_VISIBILITY = "after_published"


@weight(2)
def test_time_complexity():
    """Private test: checks whether student's code run in linear expected time"""
    rivalry_graph = dsc40graph.UndirectedGraph()
    for i in range(1_000_000):
        rivalry_graph.add_edge(str(i), str(i + 1))

    start = time.time()
    student.assign_good_and_evil(rivalry_graph)
    stop = time.time()
    elapsed_time = stop - start
    print(elapsed_time)

    assert elapsed_time < 5


@weight(2)
def test_1():
    """Private test: tests whether student returns None"""
    rivalry_graph = dsc40graph.UndirectedGraph()
    rivalry_graph.add_edge("Michigan", "OSU")
    rivalry_graph.add_edge("Michigan", "USC")
    rivalry_graph.add_edge("Michigan", "UCSD")
    rivalry_graph.add_edge("UCSD", "USC")
    rivalry_graph.add_edge("OSU", "UCSD")

    answer = assign_good_and_evil(rivalry_graph)
    student_answer = student.assign_good_and_evil(rivalry_graph)
    check_answer(rivalry_graph, student_answer, answer)


@weight(2)
def test_2():
    """Private test: tests simple graph input"""

    rivalry_graph = dsc40graph.UndirectedGraph()
    rivalry_graph.add_edge("Michigan", "UCLA")
    rivalry_graph.add_edge("Michigan", "OSU")
    rivalry_graph.add_edge("USC", "UCLA")
    rivalry_graph.add_edge("USC", "UCB")
    rivalry_graph.add_edge("OU", "OSU")

    answer = assign_good_and_evil(rivalry_graph)
    student_answer = student.assign_good_and_evil(rivalry_graph)
    check_answer(rivalry_graph, student_answer, answer)


@weight(2)
def test_3():
    """Private test: tests complicated graph input"""
    rivalry_graph = dsc40graph.UndirectedGraph()
    rivalry_graph.add_edge("UCSD", "UCLA")
    rivalry_graph.add_edge("UCSD", "Columbia")
    rivalry_graph.add_edge("UCSD", "Harvard")
    rivalry_graph.add_edge("UCLA", "UW")
    rivalry_graph.add_edge("UCLA", "Princeton")
    rivalry_graph.add_edge("Princeton", "Harvard")
    rivalry_graph.add_edge("Princeton", "Brown")
    rivalry_graph.add_edge("Harvard", "UCI")
    rivalry_graph.add_edge("UCI", "Columbia")
    rivalry_graph.add_edge("UCI", "Brown")
    rivalry_graph.add_edge("Columbia", "UW")
    rivalry_graph.add_edge("UW", "Brown")

    answer = assign_good_and_evil(rivalry_graph)
    student_answer = student.assign_good_and_evil(rivalry_graph)
    check_answer(rivalry_graph, student_answer, answer)
