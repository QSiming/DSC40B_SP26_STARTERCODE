In any case where it is not mentioned, you may assume that the graph is unweighted.

- check: does full BFS vs BFS need to be specified?

---

Suppose a hash table with 1000 bins stores 2000 numbers. Collisions are resolved with chaining. True or False: it is possible for one of the hash table's bins to contain zero elements.

(x) True
( ) False

---

Suppose a hash table is implemented so that it has ten bins, and that this number of bins is not increased when new elements are inserted; that is, the hash table is not allowed to "grow". Let $$n$$ be the number of elements stored in the hash table. What is the expected time complexity of querying an element in this hash table, as a function of $$n$$? You may assume that collisions are resolved with chaining, that the bins are linked lists, and that the hash function is "good" in that it appears to uniformly distribution elements among bins.

( ) $$Theta(1)$$
( ) $$Theta(\log n)$$
(x) $$Theta(n)$$
( ) $$Theta(n \log n)$$
( ) $$Theta(n^2)$$
( ) $$Theta(n^3)$$

---

What is the expected time complexity of the code below, assuming that `numbers` is a Python `set`? Recall that Python's `set`s are implemented as hash tables.

```
def foo(numbers):
    """Assume `numbers` is a Python `set` containing n numbers."""
    count = 0
    for x in numbers:
        if -x in numbers:
            count += 1

    return count / len(numbers)
```

( ) $$Theta(1)$$
( ) $$Theta(\log n)$$
(x) $$Theta(n)$$
( ) $$Theta(n \log n)$$
( ) $$Theta(n^2)$$
( ) $$Theta(n^3)$$

---

An undirected graph $$G = (V, E)$$ has 7 edges. What is the *smallest* number of nodes that it can have?

[____](=5+-0)

---

Let $$G = (V, E)$$ be an undirected graph. Suppose $$u$$ and $$v$$ are two nodes in $$G$$ which are in the same connected component. True or False: the edge $$(u, v)$ must be in $$G$$.

( ) True
(x) False

---

Let $$G = (V, E)$$ be an undirected graph with $$V = \{a, b, c, d, e, f, g, h\}$$
and $$E = \{ (a, f), (b, e), (b, c), (c, e), (e, d), (c, d) \}$.

How many connected components does $$G$$ have?

[____](=4+-0)

---

What is the *degree* of node $$u$$ in the graph shown below?

![](./f1.png)

[____](=6+-0)

---

Let $$G = (V, E)$$ be an (unweighted) directed graph, and let $$s$$, $$a$$, and $$b$$ be three nodes in the graph. Suppose $$(s, u_1, u_2, u_3, a, u_4, u_5, b)$$ is a shortest path from $$s$$ to $$b$$. True or False: it is possible that the shortest path distance from $$s$$ to node $$a$$ is 3.

( ) True
(x) False

---

Suppose a graph $$G = (V, E)$$ is stored using an adjacency list representation. In the worst case, what is the time complexity of finding the maximum degree of any node in the graph? You may assume that your linked list implementation stores the size of the list and can return it in constant time.

(x) $$\Theta(V)$$
( ) $$\Theta(E)$$
( ) $$\Theta(V + E)$$
( ) $$\Theta(V^2)$$
( ) $$\Theta(E^2)$$

---

Suppose a BFS is run on the graph shown below using node $$u_1$$ as the source. How many nodes are popped from the queue *before* node $$u_7$$ is popped? (Your count should include the source node itself.)

![](./f2.png)

[____](=7+-0)

---

Suppose a BFS is run on the graph shown below using node $$u_1$$ as the source. Adopt the convention that a node's neighbors are produced in ascending order by their label. What is the BFS predecessor of node $$u_8$$?

![](./f2.png)

( ) $$u_1$$
( ) $$u_2$$
( ) $$u_3$$
( ) $$u_4$$
( ) $$u_5$$
(x) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$

---

Suppose that $$s$$, $$u$$, and $$v$$ are nodes in an undirected graph $$G = (V, E)$$. Suppose that the shortest path distance from $$s$$ to $$v$$ is 4, while the shortest path distance from $$s$$ to $$v$$ is 6.

True or False: it is possible that, during a BFS using $$s$$ as the source, the pending queue contains $$u$$ and $$v$$ at the same time.

( ) True
(x) False

---

An $$n \times n$$ *lattice graph* is an undirected graph with $$n^2$$ nodes in which each node is placed on a grid, and an edge is added between the node and the nodes to the immediate north, south, east, and west. For example, a $$4 \times 4$$ lattice graph looks like this:

![](./f3.png)

What is the time complexity of BFS when run on an $$n \times n$$ lattice graph?

( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
(x) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$
( ) $$\Theta(n^4)$$

---

Suppose the code below is run on a graph $$G = (V, E)$$. What is its time complexity? You may assume that $$|E| \geq 1$$, but you should not assume anything else about the number of edges. You may assume that the graph is stored using an adjacency list representation.

```
for u in graph.nodes:
    for v in graph.neighbors(u):
        print(u, v)
```

( ) $$\Theta(E)$$
( ) $$\Theta(V)$$
(x) $$\Theta(V + E)$$
( ) $$\Theta(V^2)$$
( ) $$\Theta(V E)$$

---

Suppose $$s$$ and $$u$$ are nodes in an unweighted, undirected graph $$G = (V, E)$$, and that there are several shortest paths from $$s$$ to $$u$$. Suppose two BFSs are run starting at node $$s$$; one of them uses the convention that neighbors are produced in *ascending* order by label, and the other uses a different convention.

Which one of the following claims is true about the results?

( ) The shortest path distance to $$u$$ as well as $$u$$'s BFS predecessor must be the same in both BFSs.
( ) $$u$$'s BFS predecessor must be the same in both BFSs, but the shortest path distances to $$u$$ may be different
(x) The shortest path distance to $$u$$ must be the same in both BFSs, but $$u$$'s BFS predecessor may be different
( ) Both the shortest path distance to $$u$$ and $$u$$'s BFS predecessor may be different between the BFSs

---

Suppose a DFS is run on the graph shown below using node $$u_1$$ as the source and the convention that neighbors are produced in ascending order by label. What will be the DFS predecessor of node $$u_6$$?

![](./f2.png)

( ) $$u_1$$
( ) $$u_2$$
( ) $$u_3$$
( ) $$u_4$$
(x) $$u_5$$
( ) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$

---

Suppose $$G = (V, E)$$ is an undirected graph with 10 connected components, each of which is a tree. That is, $$G$$ is a forest of 10 trees.

What is the time complexity of full DFS when run on $$G$$?

( ) $$\Theta(1)$$
(x) $$\Theta(V)$$
( ) $$\Theta(V^2)$$
( ) $$\Theta(E^2)$$
( ) $$\Theta(V E)$$


---

Consider the code shown below. It shows DFS as seen in lecture, with one modification: a `print` statement in the for-loop.

```
def dfs(graph, u, status=None):
    """Start a DFS at `u`."""
    # initialize status if it was not passed
    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}

    status[u] = 'pending'
    for v in graph.neighbors(u):
        print("Hello!")
        if status[v] == 'undiscovered':
            dfs(graph, v, status)
    status[u] = 'visited'
```

Suppose the above code is run on the graph shown below using node $$s$$ as the source. How many times will "Hello!" be printed?

![](./f4.png)

[____](=4+-0)

---

Consider the graph below:

![](./f5.png)

Suppose a *full* DFS is run on this graph using the convention that neighbors are produced in ascending order by label. You should also assume that when the nodes of the graph are looped over, as in `for node in graph.nodes`, the nodes are also produced in ascending order by label.

What will be the start time of node $$e$$?

[____](=7+-0)

What will be the finish time of node $$a$$?

[____](=12+-0)

---

Give a topological sort of the graph from the previous problem.

|____|

---

During a call to `dfs` on a node $$u$$, 23 nodes are marked as visited, including node $$u$$ itself. What will be the difference between the finish time of $$u$$ and the start time of $$u$$? That is, what is `finish[u] - start[u]`?

[____](=45+-0)

---

Suppose a directed graph $$G$$ has $$n$$ nodes and $$n - 1$$ edges, and every node in the graph is reachable from node $$u$$.

What is the time complexity of the below code when run on this graph with node $$u$$ as the source?

```
def foo(graph, u):
    count = 1
    for v in graph.neighbors(u):
        count += foo(graph, v)
    return count
```

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
(x) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

Now suppose the directed graph $$G$$ has 90 nodes and 89 edges, and every node is reachable from node $$u$$. What is returned by `foo` when it is called on node $$u$$?

[____](=90+-0)

---

A "hub and spoke" graph with $$n$$ nodes consists of a single "hub" node, $$h$$, along with $$n - 1$$ "spoke" nodes, $$u_1, \ldots, u_{n-1}$$, and $$n - 1$$ edges from the hub node $$h$$ to each of the spoke nodes. For example, a "hub and spoke" graph with 8 nodes looks like the below:

![](./f7.png)

What is the worst case time complexity of an efficient algorithm which takes as input a hub and spoke graph and returns the label of the hub node? You may assume that the graph is represented as an adjacency list.

(x) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

Suppose the Bellman-Ford algorithm with early stopping is run on the graph shown below using node $$s$$ as the source. In the worst case, how many iterations of Bellman-Ford will be performed? That is, how many iterations of the outer `for`-loop will occur?

![](./f9.png)

[____](=4+-0)

---

Recall from before that an $$n \times n$$ *lattice graph* is an undirected graph with $$n^2$$ nodes in which each node is placed on a grid, and an edge is added between the node and the nodes to the immediate north, south, east, and west. For example, a $$4 \times 4$$ lattice graph looks like this:

![](./f3.png)

What is the time complexity of Bellman-Ford (without early stopping) when it is run on a weighted $$n \times n$$ lattice graph with no negative cycles?

( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n\log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^2 \log n)$$
( ) $$\Theta(n^3)$$
( ) $$\Theta(n^3 \log n)$$
(x) $$\Theta(n^4)$$
( ) $$\Theta(n^4 \log n)$$

---

Suppose that $$s, a, b,$$ and $$u$$ are nodes in a directed, weighted graph $$G = (V, E, \omega)$$, and that $$a$$ and $$b$$ are the only predecessors of $$u$$, as shown in the picture below:

![](./f10.png)

The cloud with the `?` is meant to represent the rest of the graph, whose structure is unknown.

Suppose the Bellman-Ford algorithm is run on $$G$$ with $$s$$ as the source. At some moment, $$u$$'s estimated predecessor is node $$a$$; that is, in the current shortest path from $$s$$ to $$u$$, node $$a$$ comes before $$u$$. Later, the algorithm is paused, and it is seen that $$u$$'s estimated predecessor is node $$b$$.

Suppose the algorithm is paused once again at a later time. True or False: it is possible that node $$u$$'s estimated predecessor is again node $$a$$. You may assume that the graph has no negative cycles.

(x) True
( ) False

---

Consider the situation described in the previous problem, except now we are running Dijkstra's algorithm. That is, suppose Dijkstra's algorithm is run on $$G$$ with $$s$$ as the source. At some moment, $$u$$'s estimated predecessor is node $$a$$; that is, in the current shortest path from $$s$$ to $$u$$, node $$a$$ comes before $$u$$. Later, the algorithm is paused, and it is seen that $$u$$'s estimated predecessor is node $$b$$.

Suppose the algorithm is paused once again at a later time. True or False: it is possible that node $$u$$'s estimated predecessor is again node $$a$$. You may assume that the graph has no negative edge weights.

( ) True
(x) False

---

Suppose a weighted graph $$G$$ contains negative edge weights, but no negative cycles. True or False: Dijkstra's algorithm is guaranteed to find the correct weighted shortest path from the source to each node in $$G$$.

( ) True
(x) False
