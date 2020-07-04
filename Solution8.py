
def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True 

sample_num = int(input('Enter a number to check if it is a prime number or not: '))

output = is_prime(sample_num)

print(output)