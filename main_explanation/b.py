# This line is to import a.py, so this file can use everything from a.py
import a

def b_function():
    print "b.py: b_function"

def b_flow():
    print "b.py: b_flow"
    b_function()
    # This function_one is from a.py
    a.function_one()

# print out __name__, this special variable will change depends on using this
# file as a standalone program or reusable module
print "b.py: __name__ =", __name__

if __name__ == "__main__":
    b_flow()