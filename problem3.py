# 3. Leap Year Explorer

# Task 1: Leap Year Checker
year = int(input('Please enter the year: '))
isDivisibleByFour = year % 4 == 0
isDivisibleByOneHundred = year % 100 == 0
isDivisibleByFourHundred = year % 400 == 0

if not isDivisibleByFour:
    print(f'{year} is not a leap year.')
elif isDivisibleByOneHundred:
    if isDivisibleByFourHundred:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
else:
    print(f'{year} is a leap year.')