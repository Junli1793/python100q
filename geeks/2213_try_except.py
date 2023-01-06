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

def try_except_else_finally(a, b):
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
        print(f"everything goes well, the result is: {c}")

    finally:
        print('This is always executed regardless of exception generation.')


print()
print("==============Example 1: No exception raised in try block==============")
try_except_else_finally(2, 3)

print()
print("==============Example 2: ZeroDivisionError exception raised==============")
try_except_else_finally(3.0, 3.0)

print()
print("==============Example 3: unknown exception raised==============")
try_except_else_finally('2', '3')

print()
print("==============Example 4: unknown exception raised==============")
try_except_else_finally(3.0, [1, 2])

print()
print("==============Example 5: unknown exception raised==============")
try_except_else_finally([1, 2], {1: 'a', 2: 'b'})
