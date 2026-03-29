1.  from collections import deque
2.
3.  def full_bfs(graph):
4.      status = {node: 'undiscovered' for node in graph.nodes}
5.      for node in graph.nodes:
6.          if status[node] == 'undiscovered'
7.              bfs(graph, node, status)
8.
9.  def bfs(graph, source, status=None):
10.     """Start a BFS at `source`."""
11.     if status is None:
12.         status = {node: 'undiscovered' for node in graph.nodes}
13.
14.     status[source] = 'pending'
15.     pending = deque([source])
16.
17.     # while there are still pending nodes
18.     while pending:
19.         u = pending.popleft()
20.         for v in graph.neighbors(u):
21.             # explore edge (u,v)
22.             if status[v] == 'undiscovered':
23.                 status[v] = 'pending'
24.                 # append to right
25.                 pending.append(v)
26.         status[u] = 'visited'
