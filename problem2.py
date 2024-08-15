# 2. The Greatest Showdown

# Task 1: Identify the Greatest
first = int(input('Please enter the first number: '))
second = int(input('Please enter the second number: '))
third = int(input('Please enter the third number: '))

if first >= second and first >= third:
    print(f'{first} is the largest number.')
elif second >= first and second >= third:
    print(f'{second} is the largest number.')
else:
    print(f'{third} is the largest number.')
    
    
# Task 2: Identify the Smallest
if first <= second and first <= third:
    print(f'{first} is the smallest number.')
elif second <= first and second <= third:
    print(f'{second} is the smallest number.')
elif third <= second and third <= third:
    print(f'{third} is the smallest number.')