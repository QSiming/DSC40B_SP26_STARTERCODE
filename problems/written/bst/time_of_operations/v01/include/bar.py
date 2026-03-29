def bar(root):
    if root is not None:
        bar(root.left)
        print(root.key)
        bar(root.right)
