import dsc40graph

def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    # TODO: Implement the biggest_descendent function
    result = {}

    def dfs(node):
        biggest = value[node]

        for child in graph.neighbors(node):
            child_biggest = dfs(child)
            if child_biggest > biggest:
                biggest = child_biggest

        result[node] = biggest
        return biggest

    dfs(root)
    return result
