def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    # TODO: Implement the assign_good_and_evil function
    labels = {}

    for start in graph.nodes:
        if start not in labels:
            labels[start] = "good"
            queue = [start]

            while queue:
                current = queue.pop(0)

                if labels[current] == "good":
                    next_label = "evil"
                else:
                    next_label = "good"

                for neighbor in graph.neighbors(current):
                    if neighbor not in labels:
                        
                        labels[neighbor] = next_label
                        queue.append(neighbor)
                    elif labels[neighbor] != next_label:
                        return None

    return labels
