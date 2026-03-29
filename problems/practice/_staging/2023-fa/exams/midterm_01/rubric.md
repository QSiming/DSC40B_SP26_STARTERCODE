# Midterm 01 Rubric

This rubric is written for Version A. The questions for Version B are in a
slightly different order, and the rubric will need to be adjusted accordingly.

If you encounter a large number of the same incorrect answer for a given
question, make a note of it. The solution could be incorrect, or we may want to
assign partial credit for that answer due to a reasonable mistake.

## Q01

+1: Theta(n^4 log n)
    
-0.1: Using something other than Theta

## Q02

+1: Theta(n^2)
    
-0.1: Using something other than Theta

## Q03

+1: Theta(n^3)
    
-0.1: Using something other than Theta


## Q04

+1: Theta(log n)
    
-0.1: Using something other than Theta


## Q05

+1: Theta(n) is the best case.
    
-0.05: Using something other than Theta (note that this is less of a penalty than above)


+1: Theta(n^2) is the worst case.
    
-0.05: Using something other than Theta (note that this is less of a penalty than above)

## Q06(a)

+1: Theta(n)
    
-0.1 for using O(). We will not take off points for using Omega.

## Q06(b)

* (+.25 point) a clear description of an algorithm that attempts to determine if the lists share an element in common
* (+.25 points) algorithm will correctly determine if the lists share an element in common
* (+.5) the algorithm has \Theta(n log n) worst case time complexity or better
* (+.4) the algorithm has Theta(n) (expected) time complexity E.g., a hash table solution will have Theta(n) expected time complexity, but we can actually do a little better.
* (+.1) the algorithm has worst case time complexity Theta(n)
* (+.5 point) stating the worst case time complexity of their algorithm

## Q07

+1: Theta(n log n)
    
-0.1: Using something other than Theta

## Q08

+1: Theta(n)
    
-0.1: Using something other than Theta.

## Q9

+.25: Has Theta(n) for the work done outside of recursive calls
    
+.25: Factor on T() is 3
    
+.25: Argument to T() is n/4
    
+.25: There are no extra terms.

## Q10

+.5: Attempts to unroll the recurrence
    
+.25: Attempts to finds a general formula
    
+.25: General formula found is T(n) = T(n/2^k) + n*(1 + 1/2 + 1/4 + ... + 1/2^{k-1}) (or very similar)
    
+.25: Attempts to solve for the k at which the base case is reached (even if general formula is incorrect)
    
+.25: Recognizes the geometric sum as Theta(1)
    
+.25: Recognizes 2^log_2 n = n, or is otherwise O(n)
    
+.25: Reaches solution of Theta(n)

## Q11

+1: True
    
## Q12

+1: O(n)

## Q13

+1: Theta(n^2)

## Q14

+.5: Answer implies an upper bound of O(sqrt{n} log n)
    
+.5: Answer implies an lower bound of Omega(sqrt{n} log n)

Theta(sqrt{n} log n) implies both of the above, and receives full credit
No credit is subtracted for an answer of "O(\sqrt n \log n) and Omega(\sqrt n \log n)"


# Q15

+1: True

## Q16

+1: True
    
## Q17

+1: True
    
## Q18

+1: True
    
## Q19

### Part a

+0.75: the elements in numbers[:odd_barrier] are odd is marked
    
+0.75: the elements in numbers[even_barrier+1:] are even is marked
    
+0.5: even_barrier - odd_barrier = n - 1 - alpha is marked
    
-.5: Each "extra" answer is marked that is not correct.

### Part b

+1: 99
+.5: 98 or 100

## Q20

+1: No: it will run without error, but arr may not be sorted when the function exits.
        
## Q21

+1: Theta(n log n)
    
-0.1: Using something other than Theta
    
## Q22

+1: Theta(log n)
    
+.25: Incorrect, but partial credit: Theta(h)

## Q23

+0.5: fewest number of time is 1
    
+0.5: greatest number of time is 10


## Q24

* (+.25 points) top level (root) of tree is correct
* (+.25 points) root's children are correct
* (+.25 points) the next level of the tree is correct
* (+.25 points) tree is correct overall
