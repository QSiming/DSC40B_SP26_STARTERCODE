Let `numbers` be a Python `set` (that is, a hash table) of size $$n$$. What is the expected time complexity of the code below?

```
def foo(numbers):
    count = 0
    for x in numbers:
        for y in numbers:
            if (x - y) in numbers:
                count = count + 1
    return count
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
(x) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

Let `numbers` be a Python `set` (that is, a hash table) of size $$n$$. What is the worst case time complexity of the code below?

```
def foo(numbers):
    count = 0
    for x in numbers:
        for y in numbers:
            if (x - y) in numbers:
                count = count + 1
    return count
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
(x) $$\Theta(n^3)$$

---

Suppose we have a hash table with 100 buckets, and the hash table is currently storing 100 elements. True or False: each bucket must contain at least one element (no matter which hash function we're using).

( ) True
(x) False

---

A directed graph has 10 nodes. What is the largest possible degree of any node in the graph?

*Hint*: don't forget about self loops.

[____](=20)

---

An undirected graph with 10 nodes is complete (meaning that it has all possible edges). What is the sum of the degrees?

[____](=90+-0)

---

Suppose an undirected graph with 25 nodes has three connected components. Suppose node $$u$$ is in the graph. What is the largest number of nodes that can possibly be reachable from $$u$$?

[____](=23)

---

Consider the directed graph $$G = (V, E)$$, with $$V = {a, b, c, d}$$ and $$E = {(c,a), (a, d), (a, b), (b, a), (a,a)}$$.

How many predecessors does node $$a$$ have in this graph?

[____](=3+-0)

---

Suppose a connected, undirected graph has $$n$$ nodes. True or False: there must be a simple path in the graph which contains all of the graph's nodes.

( ) True
(x) False

---

Suppose an undirected graph has 100 nodes. True or False: if every node has degree 49 or larger, the graph must be connected.

( ) True
(x) False

---

Let $$A$$ be the adjacency matrix of a directed graph with $$n$$ nodes. Define $$\vec e_i$$ to be the column vector with $$n$$ entries, all of them zero, except for entry $$i$$ which is one. For example, if $$n = 4$$, then $$\vec e_1 = (1, 0, 0, 0)^t$$. Let $$\vec e_i^t$$ be the transpose of this vector ($$\vec e_i^t$$ is a row vector).

For any $$i$$ and $$j$$, the vector - matrix - vector product:

$$ \vec e_i^t A \vec e_j$$

is a number. What is the correct interpretation of this number?


(x) It is 1 if the edge $$(i, j)$$ exists, and zero otherwise
( ) It is 1 if the edge $$(j, i)$$ exists, and zero otherwise
( ) It is the degree of node $$i$$
( ) It is the degree of node $$j$$
( ) It is twice the number of edges in the graph
( ) It is the number of edges in the graph

---

Suppose a breadth first search is run on the graph below using node $$g$$ as the source. What is the BFS predecessor of node $$c$$? Use the convention that the neighbors of a node are produced in alphabetical order.

( ) $$a$$
( ) $$b$$
( ) $$c$$
(x) $$d$$
( ) $$e$$
( ) $$f$$
( ) $$g$$
( ) $$h$$
( ) $$i$$

---

Suppose a depth first search is run on the graph below using node $$i$$ as the source. What is the DFS predecessor of node $$a$$? Use the convention that the neighbors of a node are produced in alphabetical order.

( ) $$a$$
( ) $$b$$
(x) $$c$$
( ) $$d$$
( ) $$e$$
( ) $$f$$
( ) $$g$$
( ) $$h$$
( ) $$i$$

---

Suppose a depth first search is run on a directed graph. True or False: it is possible that, at any moment in time, there is a node marked as visited which has a neighbor (successor) that is marked as undiscovered.

( ) True
(x) False

---

Consider the directed graph whose nodes are countries on Earth. There is an edge between nodes $$u$$ and $$v$$ if country $$u$$ exports a product to country $$v$$. Note that there are pairs of countries who both export products to one another.

Is it possible to topologically sort the nodes of this graph?

( ) Yes
(x) No

---

Consider this version of DFS which has an added print statement:

```
def dfs(graph, u, status=None):
    """Start a DFS at `u`."""
    # initialize status if it was not passed
    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}

    status[u] = 'pending'
    for v in graph.neighbors(u): # explore edge (u, v)
        if status[v] == 'undiscovered':
            print('hello')
            dfs(graph, v, status)
    status[u] = 'visited'
```

Suppose this code is run on a connected, undirected graph $$G = (V, E)$$. How many times will something be printed?

( ) $$\Theta(V)$$
( ) $$\Theta(V + E)$$
( ) $$\Theta(E)$$
( ) $$\Theta(V^2)$$

---

Suppose both BFS and DFS are run on the same graph $$G = (V, E)$$ using the same source node, $$s$$. Consider a particular node $$u$$ in the graph. True or False: The BFS predecessor found for $$u$$ and the DFS predecessor found for $$u$$ must be the same.

( ) True
(x) False

---

Suppose a depth first search is run on the graph shown below using node $$u_7$$ as the source, and adopt the convention that `graph.neighbors` produces nodes in ascending order of label. What will be the start time of node $$u_3$$?

You may assume that the start time of the source is 1.

[____](=8+-0)

---

Let $$G = (V,E)$$ be the directed graph with $$V = \{a, b, c, d, e\}$$ and $$E = \{(a, b), (b, c), (c, d)\}$$.
How many valid topological sorts of $$V$$ are there?

[____](=5+-0)

---

Suppose the code below is run on a graph G = (V, E). What is its time complexity?

```
for u in graph.nodes:
    for v in graph.edges():
        print(u, v)
```

*Hint*: be careful to make sure your answer works in the case where the graph has no edges.

( ) $$\Theta(V)$$
( ) $$\Theta(E)$$
( ) $$\Theta(V E)$$
( ) $$\Theta(V + E)$$
(x) $$\Theta(V E + V)$$
( ) $$\Theta(V E + E)$$

---

Suppose DFS is run from source node $$s$$ on a tree with 8 edges in order to compute start and finish times. What is the finish time of node $$s$$?

[____](=18+-0)

---

Suppose Bellman-Ford is run on a weighted, directed graph using node $$u$$ as the source. Assume that there are no negative cycles. True or False: After one iteration of the outer for-loop in Bellman-Ford, there must be at least one node other than $$u$$ whose estimated shortest path distance is exactly correct.

You may assume that all nodes in the graph are reachable from node $$u$$, but you should not assume that the edges of the graph are produced in any specific order.

(x) True
( ) False

---

Consider running Bellman-Ford on the graph below using node u as the source.

After three iterations of the outer for-loop, what is the estimated shortest path distance for node e?

You may assume that `graph.edges` produces edges in the following order:

$$(a, d), (a, b), (d, e), (u, c), (c, d), (b, e), (e, b), (u, a)$$

---

Suppose a directed graph $$G = (V, E)$$ is provided as an adjacency list. Define an "increasing edge" to be an edge that goes from a node with a smaller label to a node with a larger label. What is the time needed to count the number of increasing edges in the graph?

( ) $$\Theta(V)$$
(x) $$\Theta(E)$$
( ) $$\Theta(V E)$$
( ) $$\Theta(V + E)$$
( ) $$\Theta(V E + V)$$
( ) $$\Theta(V E + E)$$
