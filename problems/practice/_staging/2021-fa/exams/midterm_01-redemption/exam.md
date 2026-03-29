What is the time complexity of the following function?

```
def foo(n):
    for i in range(20):
        for j in range(math.log(n)):
            for k in range(50):
                print(i, j, k)
```

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
(x) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

What is the time complexity of the following function?

```
def foo(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                print(i, j, k)
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
(x) $$\Theta(n^3)$$

---

Suppose "arr" is an array of length "n". What is the time complexity of the following function?

```
def foo(arr):
    n = len(arr)
    i = n
    total = 0
    while i > 1:
        total += arr[i]
        i = i / 20
    return total
 
```


( ) $$\Theta(1)$$
(x) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

What is the time complexity of this function?

```
def foo(n):
    if n == 1:
        return 1
    else:
        return n * foo(n-1)
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
(x) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$
( ) $$\Theta(n!)$$

---

Let arr be an array of size n. What is the best case time complexity of the code below?

```
def foo(arr):
    for x in arr:
        for y in arr:
            if (x - y) in arr:
                return True
    return False
    ```


(x) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

Suppose "arr" is an array of length n. What is the worst case time complexity of the following function?

```
def foo(arr):
    for x in arr:
        for y in arr:
            if (x - y) in arr:
                return True
    return False
    ```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
(x) $$\Theta(n^3)$$

---

What is the worst case time complexity of this function?

```
def search_for_both(arr, x, y):
    mergesort(arr)
    ix_x = binary_search(arr, x)
    ix_y = binary_search(arr, y)
    return (ix_x is not None) and (ix_y is not None)
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
(x) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

What is the expected time complexity of the following functions, assuming that arr is an array of size n?

```
import random
import math

def foo(arr):
    n = len(arr)

    # choose a random number uniformly from the range 0, 1, ..., n-1
    x = random.randrange(0, n)

    y = 0
    if x < 1/n:
        for a in arr:
            for b in arr:
                if a + b > y:
                    y = a + b
    else:
        y = 0

    return y
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
(x) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

A maximum-sum subset of a collection of n numbers is a subset whose sum is the largest out of all possible subsets.

The brute force algorithm to find the maximum-sum subset is to consider every possible subset of the collection, compute the sum of each subset, and return the largest.

Which of the following describes the time complexity of the brute force algorithm, assuming that n is the size of the collection?


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$
( ) $$\Omega(2^n)$$

---

Suppose `arr` is an array of length $$n$$. What is the worst case time complexity of the following function?

```
import math

def median(arr):
    quicksort(arr) # sort the whole array using the quicksort algorithm
    n = len(arr)
    return arr[math.floor(n / 2)]
```


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
(x) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$

---

Consider the following recursive function.

```
import math

def foo(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]

    middle = math.floor(len(arr) / 2)
    left = arr[:middle]
    right = arr[middle:]

    total = sum(left) + sum(right)

    return foo(left) + foo(right) + total
```

What is the time complexity of this function?

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
(x) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$


---

Suppose algorithm A takes $$\Theta(n^2)$$ time, while algorithm B takes $$\Theta(n^3)$$ time.

Consider all possible arrays of size 100. True or False: there must be some input array of size 100 for which algorithm A takes less time than algorithm B.

( ) True
(x) False

---

Consider the function $$f(n) = 2n + (n + 3)log n - 30$$. Which of the following asymptotic bounds are true? Choose **all** that apply.

[x] $$\Omega(\log n)$$
[ ] $$\Theta(\log n)$$
[ ] $$O(\log n)$$
[x] $$\Omega(\sqrt n)$$
[ ] $$\Theta(\sqrt n)$$
[ ] $$O(\sqrt n)$$
[x] $$\Omega(n)$$
[ ] $$\Theta(n)$$
[ ] $$O(n)$$
[ ] $$\Omega(n \sqrt n)$$
[ ] $$\Theta(n \sqrt n)$$
[x] $$O(n \sqrt n)$$
[ ] $$\Omega(n^2)$$
[ ] $$\Theta(n^2)$$
[x] $$O(n^2)$$

---

Let $$f(n) = (n^2 + 2n - 100) \times \frac{5n^2}{n(n-1)}$$. Which of the following asymptotic bounds on $$f$$ is true?

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(\sqrt{n})$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n\sqrt{n})$$
(x) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$
( ) $$\Theta(2^n)$$

---

Give an example of a function which is $$O(n^3)$$ and $$\Omega(n^2)$$.

|____|

---

Suppose f(n) = Theta(n^3), and assume that g(n) = O(n^6) and Omega(n^4). Which one of the following is true about the product, $$f(n) \cdot g(n)$$?
Mark all that apply.

[x] $$f \cdot g = O(n^9)$$
[ ] $$f \cdot g = \Theta(n^9)$$
[x] $$f \cdot g = \Omega(n^7)$$
[x] $$f \cdot g = \Omega(n^4)$$
[ ] $$f \cdot g = \Theta(n^7)$$

---

What is the meaning of the value returned by this function?

```
def foo(arr):
    if len(arr) > 1:
        middle = math.floor(len(arr) / 2)
        left = arr[:middle]
        right = arr[middle:]
        foo(left)
        foo(right)
        merge(left, right, arr)
        return arr[middle]
```

Here, `merge` is the function used in `mergesort`; it merges two sorted arrays into arr. Also, recall that `arr[-1]` will return the last element of the array.

( ) It is the length of the input array.
( ) It is the last element of the input array (at the time the function was called)
( ) It is the minimum element of the input array.
(x) It is the median element of the input array.
( ) It is the maximum element of the input array.


---

Suppose we modify `binary_search` so that instead of using the floor operation to find the middle element of the array, we use the ceiling operation (recall that the ceiling of a number $$x$$ is the smallest integer that is $$\geq x$$). The full code is shown below for convenience:


```
def new_binary_search(arr, start, stop, target):
    if stop <= start:
        return None

    middle = math.ceil((start + stop) / 2)

    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return new_binary_search(arr, middle + 1, stop, target)
    else:
        return new_binary_search(arr, start, middle, target)
```

True or False: this modified binary search may recurse infinitely on some inputs.

(x) True
( ) False

---

Your friend has written a modified version of `mergesort` that they claim has an improved best-case time complexity:

```
def better_mergesort(arr):
    if is_already_sorted(arr):
        return
    else:
        mergesort(arr)
```

Here, `is_already_sorted` is a function that takes in an array and returns `True` if and only if the array is in sorted order. Assume that `is_already_sorted` is implemented efficiently (it has the best possible time complexity). What is the best case time complexity of `better_mergesort`?

( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
(x) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$

---

Suppose `quicksort` is coded in a way that the partition is always chosen to be the last element of the array. What will be the time taken by this version of `quicksort` on a **sorted** array of size $$n$$?


( ) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$
( ) $$\Theta(n^3)$$


---

Suppose a (not necessarily balanced) binary search tree contains 10 keys, all of them unique. True or False: it is possible for the root node of the tree to have the maximum key.

(x) True
( ) False

---

Suppose we are given a collection of $$n$$ numbers. True or False: inserting these numbers into a binary tree in sorted order results in a balanced tree.

( ) True
(x) False

---

Consider the following code which constructs a binary search tree by inserting random elements. In the best case, what is the height of the resulting BST in terms of $$n$$? Write your answer in asymptotic notation.

```
import random
def foo(n):
    bst = BinarySearchTree() # create an empty binary search tree
    for i in range(n**3): # <--- note! this is n**3
        # draw number from uniform distribution
        x = random.random()
        bst.insert(x)
    return bst
```

|____|
