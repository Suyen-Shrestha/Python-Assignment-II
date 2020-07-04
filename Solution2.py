sample_year = int(input('Enter a sample year: '))

if ((sample_year % 4 == 0 and sample_year % 100 != 0) or sample_year % 400 == 0):
    print(f'The year {sample_year} is a leap year.')
else:
    print(f'The year {sample_year} is not a leap year.')
