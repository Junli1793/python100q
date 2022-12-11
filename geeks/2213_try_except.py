"""
Python Try Except
https://www.geeksforgeeks.org/python-try-except/?ref=lbp

Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)

"""


###########
# Try Except in Python
###########

# No exception Exception raised in try block
def AbyB(a, b):
    try:
        c = ((a + b) // (a - b))

    # handles zerodivision exception
    except ZeroDivisionError:
        print("Can't divide by zero")

    except NameError:
        print("NameError Occurred and Handled")

    except:
        print("An error occurred")

    else:
        print(c)

    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')


AbyB(2.0, 3.0)
print()
AbyB(3.0, 3.0)
