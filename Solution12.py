
def check_palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False

    

sample_string = 'racecar'

print(f'The sample string for checking palindrome: {sample_string}')

if check_palindrome(sample_string):
    print('It is palindrome!')
else:
    print('It is not palindrome!')        