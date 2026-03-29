from data classes import dataclass
    @dataclass
    class Times:
        clock: int
        start: dict
        finish: dict
        
    def full_dfs_times(graph):
        status = {node:'undiscovered' for node in graph.nodes}
        predecessor = {node: None for node in graph.nodes}
        times=Times(clock=0, start={}, finish={})
        for u in graph.nodes:
            if status[u]=='undiscovered':
                dfs_times(graph, u, status, times)
        return times, predecessor
        
        def dfs_times(graph, u, status, predecessor, times):
            times.clock+=1
            times.start[u]=times.clock
            status[u]='pending'
            for v in graph.neighbors(u):
                # explore edge (u, v)
                if status[v]=='undiscovered':
                    predecessor[v]= u
                    dfs_times(graph, v, status, times)
            status[u]='visited'
            times.clock+=1
            times.finish[u]=times.clock
