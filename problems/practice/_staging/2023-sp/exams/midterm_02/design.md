## Q01
T/F it is possible for a hash table bin to contain all of the elements.

## Q02
Time complexity: imagine the hash function is faulty in that it only places items in half of the bins, but evenly.

## Q03
Time complexity: code?

## Q04
An *undirected* graph has 5 nodes. What is the greatest number of edges it can have?
Answer: 5 * 4 / 2 = 10


## Q05
A *directed* graph has 10 edges. What is the smallest number of nodes it can have?
Answer: 4

## Q06

An undirected graph with 20 nodes and 30 edges has three connected components:
A, B, and C. A has 7 nodes. What is the smallest number of edges it can have?

## Q07

Let G be this graph. How many connected components does it have?

## Q08

Suppose every node in a directed graph with > 1 node is reachable from a node
u. T/F: the in-degree of every node must be at least one.

## Q09

Consider the problem of finding a shortest path from u to v that goes through node
z. True or False: the shortest path may visit node u twice.

## Q10

Count isolated: detect the number of nodes in undirected graph that have no
neighbors. In adjacency matrix representation; adjacency list.

## Q11

BFS: how many nodes are popped from the queue before a given node?

## Q12

BFS: what is the BFS predecessor?

## Q13

T/F: it is possible that after a BFS a node's (other than the root) has a BFS predecessor with a distance equal to its own.

## Q14

Time complexity of BFS on circle graph.

## Q15

Code time complexity: modification of BFS.

## Q16

Full BFS with different order of `graph.nodes`. Is the number of calls to bfs the same?

## Q17

What will be start/finish/predecessor of node in a DFS?

## Q18

T/F: DFS with different convention, if u.start <= v.start <= v.finish <= u.finish before, it must still be the case with the new convention.

False.

## Q19

Consider the graph a -> b   c. How many valid topological sorts of this graph are there?

## Q20

Time complexity DFS on graph where u_i -> u_j iff i < j

## Q21

Suppose DFS is run from source node s s on a tree with 35 edges in order to
compute start and finish times. What is the finish time of node s s?

## Q22

BFS and DFS on tree have the same predecessors?

## Q23

What is the *fewest* number of iterations that Bellman-Ford with early stopping can do on the graph below?

## Q24

Which of the nodes below must have correctly-estimated spds after k iterations of Bellman-Ford?

## Q25

T/F: A node's predecessor may change multiple times during Bellman-Ford.
