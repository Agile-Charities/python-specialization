"""
Getting Started With Python - Functions

This is a set of exercises to help you become more comfortable with writing functions in Python. It is not part of the Coursera course. It exists only as an optional supplement.

To test your work as you progress, load this file into Python (IDLE or PyCharm)
and use your functions in the interactive Python console.
"""

# The basic structure of a Python function. It is here for reference.
def example(a, b, c = 5):
    # some work
    x = a + b

    # make sure everything is indented properly, or you will get errors
    if x > 15:
        y = x - c
    else:
        y = x + c

    # the output of the function
    return y

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
    if n % 2 == 0:
        return n / 2
    else:
        return (3*n) + 1

# Tests - uncomment to run
assert(collatz(1) == 4)
assert(collatz(4) == 2)
assert(collatz(15) == 46)
assert(collatz(31) == 94)
assert(collatz(20) == 10)

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
    result = n
    count = 0
    while result != 1:
        result = collatz(result)
        count = count + 1
    return count

# Tests - uncomment to run
assert(collatz_num(1) == 0)
assert(collatz_num(4) == 2)
assert(collatz_num(15) == 17)
assert(collatz_num(63) == 107)
assert(collatz_num(16) == 4)

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
    product = 1
    while n > 1:
        product = product * n
        n = n - 1
    return product

# Tests - uncomment to run
assert(factorial(0) == 1)
assert(factorial(1) == 1)
assert(factorial(5) == 120)
assert(factorial(10) == 3628800)
assert(factorial(20) == 2432902008176640000)

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
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

# Tests - uncomment to run
assert(fac(0) == 1)
assert(fac(1) == 1)
assert(fac(5) == 120)
assert(fac(10) == 3628800)
assert(fac(20) == 2432902008176640000)

##############
# Exercise 5 #
##############

"""
This final exercise is a bit tricky. It involves modifying a substantial
function. The function uses some Python features you have not seen before,
but you will not need to touch those features yourself. This exercise is
intended to show you how more complicated functions look and behave. The
Coursera course we follow doesn't do a particularly good job of that.

Below is an alternate way to test the above exercises. Your task is
to modify the testing code to include test numbers. That is, if the third test
fails, then the testing output should include that test 3 failed.

I have provided a run_tests() function that you can call from the Python
prompt. It will run the same tests that you used above, but it will use
the new testing method. Edit the tests in this function, and run it, to
become familiar with the expected output of the new testing method.

As far as completing the task goes, I suggest inserting the test number
into the "test failed:" string. That is, change it to "test # failed:" where
'#' is the test number.

To test your reporting, change the tests in run_tests() to be incorrect. Always
remember: tests are code too, and can have just as many errors as normal code.

Hint: don't overthink this! test() only needs a couple changes. Most of it
will stay exactly as it is now.

------------
Python features you have not encountered before:
    functions as arguments
    lambda
    fun.__name__
    multi-line strings

We can use functions as values, as long as we don't put the () at the end of them.
Using parenthesis "calls" the function, aka makes it do its thing. If we don't
call it, then it's just a (strange) Python value. Here, we pass in the function
that we want to test. We then call it from within test() by using fun(). As we
can tell from the function definition, `fun` is a variable holding the function
we pass in, therefore `fun` is the function we want to test, so we can call it.

Lambdas are "anonymous functions". You don't need to know about them, but they
are pretty cool. I suggest that you look them up, but they are not essential
to general Python usage. (I use them because they are really common in
Haskell, my favorite programming language). I use a lambda to create a
quick function that writes out the function call, but as a string.

fun.__name__ is an "attribute" that all functions have. We'll talk more about that
when we cover Object Oriented Programming (OOP) in Python. Essentially, it is
the name of the function, aka "function_name" from

def function_name():

If we have long strings, we can split them up over multiple lines by inserting \
at the end of each part, then continuing the string on a newline. As an example,
Python thinks the following two strings are equivalent:

"Sally sells sea shells."

"Sally sells" \
+ " sea" \
+ " shells."

The '+' is important, and is normal string joining.
"""

def test(fun, cases, name):
    """
    fun: the function to be tested
    cases: list of (input, expected output)
    name: the name of the set of tests
    example: test(collatz, [(15, 46), (31, 94)], "Collatz")
    """
    tst = lambda x: fun.__name__ + '(' + str(x) + ')'

    # Keep track of test number
    test_number = 0
    
    # test all provided cases
    for inp, outp in cases:
        # update our test number
        test_number += 1
        # get the function's output
        result = fun(inp)
        fails = 0
        # compare actual output to expected (test) output
        if result == outp:
            # if we're good, just move on
            pass
        else:
            # report test failure
            print name + " test " + str(test_number) + " failed: " \
                  + tst(inp) + " produced " + str(result) \
                  + ", but we expected " + str(outp)
            # keep track of how many tests have failed so far
            fails += 1

    # end of tests reporting
    if fails == 0:
        print "All " + name + " tests passed! Good work!"
    else:
        print name + " encountered " + str(fails) + " test case failures."

# These are the same tests as above, just in the new form.
# run this in the Python prompt
def run_tests():
    # You'll want to edit the stuff in the parenthesis. Each set of parenthesis
    # is an (input, expected output) - aka a test case. If that's unclear,
    # compare them to the assert() tests above to figure out which parts change
    test(collatz,
         [(1,4), (4,2), (15,46), (31,94), (20,10)],
         "Collatz")
    test(collatz_num,
         [(1,0), (4,2), (15,17), (63,107), (16,4)],
         "Collatz Number")
    test(factorial,
         [(0,1), (1,1), (5,120), (10,3628800), (20,2432902008176640000)],
         "Factorial (Loop)")
    test(fac,
         [(0,1), (1,1), (5,120), (10,3628800), (20,2432902008176640000)],
         "Factorial (Recursion)")
