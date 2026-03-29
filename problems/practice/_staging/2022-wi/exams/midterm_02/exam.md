Midterm 02
==========

This is the midterm exam written in Gradescope online assignment format.
Problems are separated by `---`.

Topics: Lecture 09 through Lecture 14 (hashing through Bellman-Ford).

--- 0

### Honor Code

I understand that I must not talk to anyone else about this exam before it has been graded. I also understand that talking to someone else during the exam would be not only an academic integrity violation, but also be a violation of the trust placed in me by the course staff.

--- 1

Suppose $$T$$ is a hash table of size 100 (that is, it has 100 bins). 300 elements are inserted into the hash table using a hash function that satisfies the uniform hashing assumption (that is, any element is equally-likely to hash into any bin). What is the expected number of elements in the first bin?

[____](=3)

--- 2

Suppose a hash table is constructed using linked lists to store the data within each bin, and that collisions are resolved by chaining. What is the *worst case* time complexity of inserting a new element into the hash table? You may assume that the hash table will not need to be resized, and that evaluating the hash function takes $$\Theta(1)$$ time.

(x) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$

--- 3

Suppose $$u$$ is a node in a complete, undirected graph $$G = (V,E)$$. What is the degree of $$u$$? Remember, an undirected graph is *complete* if it contains every possible edge.

( ) $$|V|$$
( ) $$|E|$$
(x) $$|V| - 1$$
( ) $$|E| - 1$$
( ) $$|V|^2$$

--- 4

Let $$V = \{a, b, c, d\}$$ and $$E = {(a,b), (a,a), (a,c), (d,b), (c,a)}$$ be the nodes and edges of a directed graph. How many predecessors does node $$b$$ have?


[____](=2)

--- 5

Let $$C$$ be a connected component in an undirected graph $$G$$. Suppose $$u_1$$ is a node in $$C$$ and let $$u_2$$ be a node that is reachable from $$u_1$$. True or False: $$u_2$$ must also be in the same connected component, $$C$$.

(x) True
( ) False

--- 6

Let $$A$$ be the adjacency matrix representing a directed graph with $n$ nodes. What is the greatest possible sum of any *row* of $$A$$?

( ) $$1$$
( ) $$n - 1$$
(x) $$n$$
( ) $$n^2 - 1$$
( ) $$n^2$$

--- 7

Let $$G = (V, E)$$ be a connected, undirected graph with 16 nodes and 35 edges. What is the greatest possible number of edges that can be in a simple path within $$G$$?

[____](=15)

--- 8

Suppose $$G = (V, E)$$ is an undirected graph. Let $$k$$ be the number of connected components in $$G$$. True or False: it is possible that $$k > |E|$$.

(x) True
( ) False

--- 9

Let $$G = (V, E)$$ be a *directed* graph, and suppose $$u, v, w \in V$ are all nodes. True or False: if $$w$$ is reachable from $$v$$, and $$v$$ is reachable from $$u$$, then $$w$$ is reachable from $$u$$.

(x) True
( ) False

--- 10

Let $$G = (V,E)$$ be a connected, undirected graph with $$|E| = |V| - 1$$. Suppose $$u$$ and $v$$ are both nodes in $$G$$. True or False: there can be more that one simple path from $$u$$ to $$v$$.

( ) True
(x) False

--- 11

Suppose an undirected graph $G = (V,E)$ has two connected components, $$C_1$$ and $$C_2$$. Suppose that $$|C_1| = 4$$ and $$|C_2| = 3$$. What is the largest that $$|E|$$ can possibly be?

[____](=25)

--- 12

Suppose a *breadth* first search (BFS) is run on the graph shown below using node $$u_4$$ as the source and the convention that `graph.neighbors` produces nodes in ascending order by label. What will be the predecessor of $$u_6$$ in the BFS?

<f1>

( ) $$u_1$$
(x) $$u_2$$
( ) $$u_3$$
( ) $$u_4$$
( ) $$u_5$$
( ) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$
( ) $$u_9$$

--- 13

Suppose a *depth* first search (DFS) is run on the graph shown below using node $$u_4$$ as the source and the convention that `graph.neighbors` produces nodes in ascending order by label. What will be the predecessor of $$u_6$$ in the DFS?

<f1>

( ) $$u_1$$
( ) $$u_2$$
(x) $$u_3$$
( ) $$u_4$$
( ) $$u_5$$
( ) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$
( ) $$u_9$$

--- 14

Suppose a *breadth* first search (BFS) is run on a graph $G = (V, E)$, and that node $$u$$ is distance 5 from the source while node $$v$$ is distance 3 from the source. True or False: it is possible that at some point during the BFS, both $$u$$ and $$v$$ are in the pending queue at the same time.

( ) True
(x) False

--- 15

Suppose the code below is run on a graph $$G = (V, E)$$. What is its time complexity? You may assume that $|E| \geq 1$$.

```
for u in graph.nodes:
    for v in graph.neighbors(u):
        print(u, v)
```

( ) $$\Theta(E)$$
( ) $$\Theta(V)$$
(x) $$\Theta(V + E)$$
( ) $$\Theta(V^2)$$
( ) $$\Theta(VE)$$

--- 16

Consider the modified version of BFS shown below. It is the same as the code shown in lecture, except a single `print("Here!")`-statement has been added.


```
def bfs(graph, source):
    """Start a BFS at `source`."""
    status = {node: 'undiscovered' for node in graph.nodes}
    status[source] = 'pending'
    pending = deque([source])

    # while there are still pending nodes
    while pending: 
        u = pending.popleft()
        for v in graph.neighbors(u):
            # explore edge (u,v)
            if status[v] == 'undiscovered':
                print('Here!')
                status[v] = 'pending'
                # append to right
                pending.append(v)
        status[u] = 'visited'
```

Suppose this function is run on the graph shown below using node $$u_4$$ as the source. Exactly how many times will "Here!" be printed?

[____](=8)

--- 17

What is the time complexity of depth first search (DFS) when run on a tree with $n$ nodes?

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
(x) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

--- 18

Suppose a *depth* first search is run on a directed graph. True or False: it is possible that, at any moment in time, there is a node marked as visited which has a neighbor (successor) that is marked as pending.

(x) True
( ) False

--- 19

Suppose a depth first search is run on the graph shown below using node $$u_4$$ as the source, and adopt the convention that `graph.neighbors` produces nodes in ascending order of label. Which node will have the smallest finish time?


(x) $$u_1$$
( ) $$u_2$$
( ) $$u_3$$
( ) $$u_4$$
( ) $$u_5$$
( ) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$
( ) $$u_9$$

--- 20

Suppose a depth first search is run on the graph shown below using node $$u_4$$ as the source, and adopt the convention that `graph.neighbors` produces nodes in ascending order of label. What will be the start time of node $$u_7$$?

[____](=10)

--- 21

Let $$G = (V,E)$$ be the directed graph with $V = \{a, b, c, d, e\}$ and $E = \{(a, b), (a, c), (a, d), (b, e), (c, e), (d, e)\}$.
How many valid topological sorts of $V$ are there?

[____](=6)

--- 22

Suppose T = (V, E) is a connected, undirected graph with no cycles (that is, T is a tree). Suppose a depth first search is run on T using node s as the source. Assume that node s has two neighbors: u and v. If |V| = 15, which one of the below represents possible start and finish times of u and v? You may assume that `graph.neighbors` produces neighbors in ascending order of label.

( ) `start[u] = 2`, `finish[u] = 10`, `start[v] = 8`, `finish[v] = 29`
(x) `start[u] = 2`, `finish[u] = 21`, `start[v] = 22`, `finish[v] = 29`
( ) `start[u] = 1`, `finish[u] = 16`, `start[v] = 17`, `finish[v] = 30`
( ) `start[u] = 16`, `finish[u] = 29`, `start[v] = 2`, `finish[v] = 15`


--- 23

Suppose Bellman-Ford is run on the graph below using node $$a$$ as the source, and assume that edges are updated in the following order:

(a, b), (a, c), (a, d), (b, h), (e, h), (c, e), (f, g), (d, f), (g, h)

After three iterations of the outer loop (that is, after updating all edges three times), what is the estimate shortest path distance to node $$h$$?

[____](=1)


--- 24

Recall that Bellman-Ford with early stopping updates edges iteratively until no estimated distances change, at which point the algorithm terminates early. True or False: the number of iterations needed before early termination may depend on the order in which the edges are updated.

(x) True
( ) False

--- 25

Suppose that every edge in the weighted graph $$G$$ has weight -5. True or False: breadth first search on this graph will compute a *longest* path from the source to every node in the graph (that is, a path with greatest possible total edge weight).

You may assume that every node in the graph is reachable from the source.

(x) True
( ) False
