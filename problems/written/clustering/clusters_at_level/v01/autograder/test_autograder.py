import dsctest
import dsc40graph
from collections import deque
from gradescope_utils.autograder_utils.decorators import weight, visibility

import numpy as np


def symmetrize(dct):
    def func(u, v):
        if (u, v) in dct:
            return dct[(u, v)]
        else:
            return dct[(v, u)]
    return func


class Test(dsctest.CodeTestCase):

    @weight(1)
    @visibility('visible')
    def test_named_correctly(self):
        self.assert_module_name_correct('cluster')
        import cluster
        self.assert_function_name_correct(cluster, 'cluster')

    @weight(1)
    @visibility('visible')
    def test_function_on_simple_example(self):

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


        import cluster
        self.assert_answer_equals(
                cluster.cluster,
                args=[graph, weights, .4],
                expected_output=frozenset([
                        frozenset(['a', 'b']),
                        frozenset(['c', 'd'])
                    ])
                )

    @weight(1)
    @visibility('after_published')
    def test_with_edge_equal_to_level(self):

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


        import cluster
        self.assert_answer_equals(
                cluster.cluster,
                args=[graph, weights, .3],
                expected_output=frozenset([
                        frozenset(['a', 'b', 'c', 'd']),
                    ])
                )

    @weight(1)
    @visibility('after_published')
    def test_with_three_clusters(self):

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


        import cluster
        self.assert_answer_equals(
                cluster.cluster,
                args=[graph, weights, .4],
                expected_output=frozenset([
                        frozenset(['a', 'b']),
                        frozenset(['c', 'd']),
                        frozenset(['e', 'f', 'g']),
                    ])
                )
    @weight(1)
    @visibility('after_published')
    def test_with_high_level_so_each_node_is_a_cluster(self):

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


        import cluster
        self.assert_answer_equals(
                cluster.cluster,
                args=[graph, weights, 1],
                expected_output=frozenset([
                        frozenset(['a']),
                        frozenset(['b']),
                        frozenset(['c']),
                        frozenset(['d']),
                        frozenset(['e']),
                        frozenset(['f']),
                        frozenset(['g']),
                    ])
                )

    @weight(1)
    @visibility('after_published')
    def test_with_low_level(self):

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


        import cluster
        self.assert_answer_equals(
                cluster.cluster,
                args=[graph, weights, .01],
                expected_output=frozenset([
                        frozenset(['a', 'b', 'c', 'd']),
                        frozenset(['e', 'f', 'g']),
                    ])
                )
