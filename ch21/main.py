
# execution

from calculator import Calculator

def is_well_formed(equation):
    parsed_eq = equation.split(' ')
    return len(parsed_eq) == 3

def main():
    c = Calculator()
    while (True):
        equation = raw_input("Enter equation for calculation with operator first "
                                + "(i.e. + 1 2):\n")
        if (is_well_formed(equation)):
            # parse data (get operator and values)
            parsed_eq = equation.split(' ')
            op = parsed_eq[0]
            val1 = int(parsed_eq[1])
            val2 = int(parsed_eq[2])

            if (op == "+"):
                print ('\n' + str(c.add(val1, val2)) + '\n')
            elif (op == "-"):
                print ('\n' + str(c.subtract(val1, val2)) + '\n')
            elif (op == "*"):
                print ('\n' + str(c.multiply(val1, val2)) + '\n')
            elif (op == "/"):
                print ('\n' + str(c.divide(val1, val2)) + '\n')
            else:
                print '\ninvalid operator\n'

        else:
            print '\ninvalid format\n'



if __name__ == '__main__':
    main()
