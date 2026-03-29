import soln

def test_simple():
    arr = [1, 3, 5, 6, 7, 9, 12]
    root = soln.build_balanced_bst(arr, 0, len(arr))
    assert root.key  == 6
    assert root.left.key == 3
    assert root.left.left.key == 1
    assert root.left.right.key == 5
    assert root.right.key == 9
