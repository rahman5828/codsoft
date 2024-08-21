import math 

def add(first_number, second_number):
    return first_number + second_number



def subtract(first_number, second_number):
    return first_number - second_number



def multiply(first_number, second_number):
    return first_number * second_number



def divide(first_number, second_number):
    return first_number / second_number


while True:
    
    choice = input('Enter choice(1/2/3/4 or n to cancel): ')
    
    if choice in ('1', '2', '3', '4'):
        first_number = float(input('Enter first number: '))
        second_number = float(input('Enter second number: '))

        if choice == '1':
            print(first_number, '+', second_number, '=', add(first_number, second_number))

        elif choice == '2':
            print(first_number, '-', second_number, '=', subtract(first_number, second_number))

        elif choice == '3':
            print(first_number, '*', second_number, '=', multiply(first_number, second_number))

        elif choice == '4':
            print(first_number, '/', second_number, '=', divide(first_number, second_number))
    elif choice == 'n':
        print('Your are successfully logged out!')
        break
    else:
        print('Please enter correct input among these 1/2/3/4/n')
