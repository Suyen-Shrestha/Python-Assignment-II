
def calculation(num1,num2,operator):
    if operator == '+':
            return num1 + num2
    elif operator == '-':
            return num1 - num2
    elif operator == '*':
            return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            print('Division by Zero!')
            return None    
    else:
        return None           



try:
    first_num = int(input('Enter the first number: '))
    second_num = int(input('Enter the second number: '))
except:
    print('The input is not a number!')


print("""Please select operation -\n 
        '+' for Add \n 
        '-' for Subtract\n
        '*' for Multiply\n 
        '/' for Divide\n""")

try:
    operator = input('Enter an operator for calculation: ')
    if operator not in ('+','-','*','/'):
        raise ValueError
except ValueError:
    print('Invalid Option!')


output = calculation(first_num,second_num,operator)
print(output)

 
    

