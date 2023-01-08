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
    except ZeroDivisionError as err:
        print(err)
        print("Can't divide by zero")

    except NameError as err:
        print(err)
        print("NameError Occurred and Handled")

    except Exception as err:
        print("An error occurred: ", err)

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

print(type(2.0))
print(type(2))
print(type(3/2))
print(type(3//2))
print(type(complex(2, 2)))
print(type(True))
print(type("2"))
print(type(["2"]))
print(type({1: 'a', 2: 'b'}))
