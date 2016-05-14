def function_one():
    print "a.py: function_one"

def execution_flow():
    print "a.py: execution_flow"
    function_one()

# print out __name__, this special variable will change depends on using this
# file as a standalone program or reusable module
print "a.py: __name__ =", __name__

if __name__ == "__main__":
    execution_flow()