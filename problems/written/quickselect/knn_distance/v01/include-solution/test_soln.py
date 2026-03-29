import knn_distance


def test_simple():
    
    arr = [3, 10, 15, 52]
    q = 19

    assert knn_distance.knn_distance(arr, q, 1) == (4, 15)
    assert knn_distance.knn_distance(arr, q, 2) == (9, 10)
    assert knn_distance.knn_distance(arr, q, 3) == (16, 3)
