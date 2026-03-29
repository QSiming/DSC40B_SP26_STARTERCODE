def foo(root):
    node = root
    while node is not None:
        parent = node.parent
        node = node.left
    return parent.key
