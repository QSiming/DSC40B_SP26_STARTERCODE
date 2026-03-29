class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_balanced_bst(sorted_arr, start, stop):
    if stop - start <= 0:
        return None

    mid_ix = (start + stop) // 2
    median = sorted_arr[mid_ix]
    root = Node(median)

    root.left = build_balanced_bst(sorted_arr, start, mid_ix)
    root.right = build_balanced_bst(sorted_arr, mid_ix + 1, stop)

    return root
