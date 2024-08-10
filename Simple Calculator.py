class MathematicalOperators:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.....")
        return x / y


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input! Please enter a number.')


math = MathematicalOperators()

print('''Supported operations
a - addition
s - subtraction
m - multiplication
d - division
q - quit''')

number1 = get_number('Please type first number: ')
number2 = get_number('Please type second number: ')

while True:
    operation_opted_by_user = input('Choose the operation you want to perform: ').lower()
    if operation_opted_by_user == 'q':
        print("Goodbye!")
        break
    try:
        if operation_opted_by_user == 'a':
            print(f'Your result: {math.add(number1, number2)}')
        elif operation_opted_by_user == 's':
            print(f'Your result: {math.subtract(number1, number2)}')
        elif operation_opted_by_user == 'm':
            print(f'Your result: {math.multiply(number1, number2)}')
        elif operation_opted_by_user == 'd':
            if number2 == 0:
                number2 = get_number('Second number cannot be 0 for division. Re-enter your second number: ')
            print(f'Your result: {math.divide(number1, number2)}')
        else:
            print('⚠️ Please choose a valid operation (a, s, m, d, q)')
    except ZeroDivisionError as e:
        print(f'ERROR: {e}')


   
