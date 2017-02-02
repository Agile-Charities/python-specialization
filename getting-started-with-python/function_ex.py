"""
Getting Started With Python - Functions

This is a set of exercises to help you become more comfortable with writing functions in Python. It is not part of the Coursera course. It exists only as an optional supplement.

To test your work as you progress, load this file into Python (IDLE or PyCharm)
and use your functions in the interactive Python console.
"""

# The basic structure of a Python function. It is here for reference.
def example(a, b, c = 5):
    # do some work
    x = a + b

    # make sure everything is indented properly, or you will get errors
    if x > 15:
        y = x - c
    else:
        y = x + c

    # the output of the function
    return y

assert(example(1,2,3) == 6)
"""
Some tests will be beneath each function. If the tests pass, they will be silent.
If, however, they fail, then they will produce an AssertionError like the following:

Traceback (most recent call last):
  File "ex_function.py", line 131, in <module>
    assert(factorial(5) == 121)
AssertionError

This just means that the stuff inside of assert() did not evaluate to True. (In
this particular case, factorial(5) == 120. You'll be writing this function!).

Note that the error tells you what line number the test is on. This makes it easy to jump to the exact test that your function failed.

Assertions are hardcore. If an assertion fails, Python will not load your file. If
you get stuck on an assertion, feel free to comment it out while you continue working.

By default, none of the functions are implemented, so all of the assertions will
fail. I have therefore left all of the assertions commented out. To run the tests,
delete the '#' character in front of the assert() calls.
"""

##############
# Exercise 1 #
##############

"""
This function will perform a simple calculation on a single number.
This function takes a single numbre (integer) as input.
Only worry about positive numbers - forget about negatives.
This function produces a single number as output.
If the input is even, divide it by 2.
If the input is odd, multiply it by 3 and then add 1.
Return the result.
"""
def collatz(n):
    pass

# Tests - uncomment to run
#assert(collatz(1) == 4)
#assert(collatz(4) == 2)
#assert(collatz(15) == 46)
#assert(collatz(31) == 94)
#assert(collatz(20) == 10)

##############
# Exercise 2 #
##############

"""
This function will repeatedly apply the collatz() function to its input, until
it produces the value of 1.
It takes as input a single number.
It will count how many times collatz() needs to be applied before the number
reaches 1.
It will return the count as its output.
Hint: use a count variable
Hint: use a while loop
If the output seems interesting, check out the Collatz Conjecture on wikipedia.
"""
def collatz_num(n):
    pass

# Tests - uncomment to run
#assert(collatz_num(1) == 0)
#assert(collatz_num(4) == 2)
#assert(collatz_num(15) == 17)
#assert(collatz_num(63) == 107)
#assert(collatz_num(16) == 4)

##############
# Exercise 3 #
##############

"""
Factorial
The factorial of an integer is that number times all the other integers less than
it, down to one. factorial(0) is defined to be 1. Ignore negative numbers.

Example: factorial(0) == 1
Example: factorial(1) == 1
Example: factorial(2) == 2 * 1
Example: factorial(3) == 3 * 2 * 1
Example: factorial(10) == 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

Note: in this exercise, you should use a loop. The next exercise will not use a loop.
Note: be careful with big numbers. Glance down at the test for factorial(20).
      These outputs get big, fast.
"""
def factorial(n):
    pass

# Tests - uncomment to run
#assert(factorial(0) == 1)
#assert(factorial(1) == 1)
#assert(factorial(5) == 120)
#assert(factorial(10) == 3628800)
#assert(factorial(20) == 2432902008176640000)

##############
# Exercise 4 #
##############

"""
Implement the factorial behavior without using a loop. The core concept here is
called "recursion", and involves calling fac() from inside itself.
Hint: return n * fac(n-1)
Hint: if it doesn't ever finish, you forgot to put it in an if statement.
      (or your if statement isn't doing what you thought it was doing)
      Use Ctrl-C a couple times to make it cancel running.
"""
def fac(n):
    pass

# Tests - uncomment to run
#assert(fac(0) == 1)
#assert(fac(1) == 1)
#assert(fac(5) == 120)
#assert(fac(10) == 3628800)
#assert(fac(20) == 2432902008176640000)

