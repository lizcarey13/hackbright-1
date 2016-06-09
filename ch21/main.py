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

            result = c.dispatch(op)(val1, val2)
            if result is None:
                print '\ninvalid operator\n'
            else:
                print ('\n' + str(result) + '\n')
        else:
            print '\ninvalid format\n'



if __name__ == '__main__':
    main()
