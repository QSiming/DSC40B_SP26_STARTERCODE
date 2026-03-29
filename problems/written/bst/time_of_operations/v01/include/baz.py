def baz(root, key):
    current_node = root
    current_ceil = None
    while current_node is not None:
        if current_node.key == key:
            return current_node
        elif current_node.key > key:
            current_ceil = current_node
            current_node = current_node.left
        else:
            current_node = current_node.right
            
    if current_ceil is None:
        raise ValueError(f'{key} has no ceiling.')
        
    return current_ceil
