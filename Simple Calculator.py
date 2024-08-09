class MathematicalOperators:
    def add(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x/y


math = MathematicalOperators()
number1 = int(input('Please type first number: '))
number2 = int(input('Please type second number: '))
operation_opted_by_user = str(input('''a - Addition
s - Subtraction
m - Multiplication
d - Division
Choose the operation you want to perform: ''')).lower()
try:
    if operation_opted_by_user == 'a':
        print(f'your result: {math.add(number1, number2)}')
    elif operation_opted_by_user == 's':
        print(f'your result: {math.subtraction(number1, number2)}')
    elif operation_opted_by_user == 'm':
        print(f'your result: {math.multiply(number1, number2)}')
    elif operation_opted_by_user == 'd':
        print(f'your result: {math.divide(number1, number2)}')
    else:
        print(f'⚠️Please choose an operation mentioned above')
except ZeroDivisionError:
    print(f'ERROR: If you want to perform Division then your second number cannot be 0.')

# actions to perform : integrate a while loop
# counter the expected errors
# add information about the result i.e.  it is an integer or a rational number etc.
