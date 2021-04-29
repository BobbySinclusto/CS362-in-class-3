def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    raise TypeError('Arguments must be numbers.')

def subtract(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a - b
    raise TypeError('Arguments must be numbers.')

def multiply(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a * b
    raise TypeError('Arguments must be numbers.')

def divide(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if b != 0:
            return a / b
        raise ZeroDivisionError('Cannot divide by Zero.')
    raise TypeError('Arguments must be numbers.')

if __name__ == '__main__':
    print('Welcome to the calculator! Please choose an option.')
    while (True):
        print(
'''
Choose an option:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Quit''')
        choice = input()

        if choice == '1':
            print(f'Result: {add(eval(input("First number: ")) , eval(input("Second number: ")))}')
        elif choice == '2':
            print(f'Result: {subtract(eval(input("First number: ")) , eval(input("Second number: ")))}')
        elif choice == '3':
            print(f'Result: {multiply(eval(input("First number: ")) , eval(input("Second number: ")))}')
        elif choice == '4':
            print(f'Result: {divide(eval(input("First number: ")) , eval(input("Second number: ")))}')
        else:
            break