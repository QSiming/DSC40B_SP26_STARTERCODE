Midterm 01
==========

Covers Lectures 01--09 (up to BSTs).

## Section 1: Time Complexity

- Simple nested loops
- Inner loop depends on outer loop, leading to 1 + 2 + ... + n
- "Ugly" bounds for inner/outer loops, such as `range(n**2 + log(n) + 42)`
- Code using "built in" functions/operators like `in`, `sum()`, etc.
- While-loop with geometrically increasing counter. (logarithmic time)
- Best/worst case for if-then-else, perhaps within a loop.
- Simple expected time complexity.
- State the recurrence relation for this piece of code.
- Determine the time complexity of this recursive code (requires solving recurrence).
- Multivariate time complexity.
- Theoretical lower bound for a problem.

- (Optional) Is it possible for an exponential time algorithm to be "faster" than a
  O(n^2) algorithm?
- (Optional) Inner loop depends on outer loop, leading to log(1) + log(2) + ... + log(n)

## Section 2: Asymptotic Notation

- Choose all which apply for a given function (Theta, Big Oh, Big Omega). (Probably want
  several of these).
- Is this property true? E.g., f = Theta(n^2) and f = Omega(n) so f = n^2 or f = n
    - which of these properties are true in general? choose all that apply
- Adding asymptotic notation. E.g., Theta(n^2) + Omega(n^3) = ?


## Section 3: Recursion, Binary Search, Mergesort, Quickselect

- How many calls will be made for this recursive code? (how many times is this printed?)
- What does this modified version of Quickselect/Mergesort/Binary Search do?
- What is the time complexity of this modified version of Quickselect/Mergesort/Binary Search?
- Best case/worst case for code that calls a binary search/quickselect/mergesort
- Identify the bug in this recursive code.

## Section 4: Binary Search Trees

- How large can the tree be if balanced/unbalanced? (Can test by inserting a print into
  query code, asking how many lines are printed at most/at least.)
- Invariant about a query. E.g., suppose the root is 42. We query for 33. Is it ever
  possible to find a node that is larger than 42 on the way down to 33? What about
  larger than 33?
- Question on the BST property. E.g., is it sufficient for every left child < parent and right child
  > parent to be a BST? Or, more simply, given a picture: is this a BST?
