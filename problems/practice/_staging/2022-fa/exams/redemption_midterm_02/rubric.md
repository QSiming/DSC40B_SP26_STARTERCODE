# Midterm 01 Rubric

This rubric is written for Version A. The questions for Version B are in a
slightly different order, and the rubric will need to be adjusted accordingly.

If you encounter a large number of the same incorrect answer for a given
question, make a note of it. The solution could be incorrect, or we may want to
assign partial credit for that answer due to a reasonable mistake.

## Q01

+ 1: Theta(n^4)

## Q02

+ 1: Theta(n^2)
- 0.1: Using something other than Theta

## Q03

+ 1: Theta(n^2 * sqrt(n))
- 0.1: Using something other than Theta


## Q04

+ 1: Theta(n)
- 0.1: Using something other than Theta


## Q05

+ 1: Theta(n)
- 0.05: Using something other than Theta (note that this is less of a penalty than above)

## Q06

+ 1: Theta(n^2)
- 0.05: Using something other than Theta (note that this is less of a penalty than above)

## Q07

+ 1: Theta(n)
- 0.1 for using O(). We will not take off points for using Omega.

## Q08

+ 0.75: Theta(log n)
+ 0.25: Theta(n)
+ 0.25: Theta(1)

+ 0.75: A modified binary search is described.
+ 0.25: A linear search is described.
+ 0.25: A version of "we check the item 10 from the back of the array" is described. This can only tell us whether or not there are >= 10 elements within 10 of the max; it does not count them.

+ 0.5: Described algorithm has the time complexity that was answered above.

## Q09

+ 1: Theta(sqrt(n))
- 0.1: Using something other than Theta.

## Q10

+ 1: Theta(n^2)
+ 0.5: Theta(n^2)
- 0.1: Using something other than Theta.

## Q11

+1: True

## Q12

+.5: Has Theta(n) for the work done outside of recursive calls
+.25: Factor on T() is 6
+.25: Argument to T() is n/3
-.25: There are extra terms.

## Q13

+.5: Attempts to unroll the recurrence
+.25: Attempts to finds a general formula
+.25: General formula found is T(n) = 2^k T(n/4^k) + n*(1 + 1/2 + 1/4 + ... + 1/2^{k-1}) (or very similar)
+.25: Attempts to solve for the k at which the base case is reached (even if general formula is incorrect)
+.25: Recognizes the geometric sum as Theta(1)
+.25: Recognizes 2^log_4 n = sqrt(n), or is otherwise O(n)
+.25: Reaches solution of Theta(n)

## Q14

+1: False

## Q15

+1: True

## Q16

+1: True

## Q17

+1: False

## Q18

+.5: Answer implies an upper bound of O(n^3)
+.5: Answer implies an lower bound of Omega(n^3)

Theta(n^3) implies both of the above, and receives full credit
No credit is subtracted for an answer of "O(n^3) and Omega(n^3)"

## Q19

+.5: An upper bound of O(n^5)
+.5: An lower bound of Omega(n^4)

## Q20

+1: False

## Q21

+.5: arr[:start] < t
+.5: arr[stop:] > t
-.5: An "extra" answer is marked that is not correct.

## Q22

Three parts; one for each recursive call:

When `arr[middle] == t`:

+.25: Recursive call with `start=start`
+.25: Recursive call with `stop=middle`
+.5: Recursive call with `last_seen=middle`

One of the recursive calls has:

+.25: Recursive call with `start=middle+1`
+.25: Recursive call with `stop=stop`
+.25: Recursive call with `last_seen=last_seen`
+.25: If this call is when `arr[middle] < t`

Another of the recursive calls

+.25: Recursive call with `start=start`
+.25: Recursive call with `stop=middle`
+.25: Recursive call with `last_seen=last_seen`
+.25: If this call is when `arr[middle] > t` (i.e., in the `else`)

## Q23

+1: Theta(n)

## Q24

+1: Will recurse infinitely (or raise an error due to infinite recursion)
+.75: Partial: Mentions that a base case is missing, but does not say what will happen

## Q25

+1: False

## Q26

+1: Theta(n)
+.25: Incorrect, but partial credit: Theta(log n)
+.25: Incorrect, but partial credit: Theta(h)

We will not take off for using something other than Theta.

## Q27

+.25: First number is inserted correctly
+.25: Second number is inserted correctly (relative to where first number was placed)
+.25: Third number is inserted correctly (relative to where first two numbers were placed)
+.25: Result is a valid BST

It may happen that the student's first (or second) insertion is incorrect, but
we can still grade the following insertion(s) for partial credit. For example,
to grade the second insertion when the first was incorrect, assume that you are
given a tree without the second and third numbers, but with the first number
where the student placed it. Imagine inserting the second number into this tree
-- if it ends up where the student put it, give credit for the second rubric
item.
