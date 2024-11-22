
import re
import ipdb as ipdb


class MyCalculator(Exception):

    previous = 0

    # Multiplication function
    def product(x, y):
        return x*y

    # Division function
    def division(x, y):
        return x/y
    # Addition function
    def add(x, y):
        return x+y

    def difference(x, y):
        return x-y

    try:
        print('Enter your expression:')
        x = input()
        # split the string expression as an array list
        items = re.split(r'([+ - * /])', x)
        print(items)
        # Verify that list has more than one item
        while len(items) > 1:
            # set operator found as false
            operator_found = False
            # Iterate through the expression and check for opearion in the order given
            for i in range(0, len(items)-1):
                if items[i] == '/':
                    operator_found = True
                    res = division(int(items[i - 1]), int(items[i + 1]))
                    break
                elif items[i] == '*':
                    operator_found = True
                    res = product(int(items[i - 1]), int(items[i + 1]))
                    break
                elif items[i] == '+':
                    operator_found = True
                    res = add(int(items[i - 1]), int(items[i + 1]))
                    break
                elif items[i] == '-':
                    operator_found = True
                    res = difference(int(items[i - 1]), int(items[i + 1]))
                    break
                else:
                    print(items[i])
                # When operation found, delete 3 items from the list and insert the result in that place
            if operator_found:
                del items[i - 1:i + 2]
                items.insert(i - 1, res)


        print(items)


    except(Exception):
        print("Exception occurred:", Exception)









