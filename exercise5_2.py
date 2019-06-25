

'''Solution by Amon Ochuka
Write a program that repeatedly prompts a user for integer numbers until 
the user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it with 
a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 
10, and 4 and match the output below.
Invalid input
Maximum is 10
Minimum is 2
'''
# Handles the special case for the first input
num = input('Enter a number: ')
if num == 'done':
    quit()                                # Exits if no input

number = float(num)          # Ensure input is a float

smallest = number
largest = number

while True:                               # Stays in loop until break
    num = input('Enter a number: ')
    if num == 'done':
        break                             # Exits loop
    try:
        number = float(num)      # Ensure input is a float
    except:
        print ('Invalid Input')
        break
    if number > largest:                  # Condition for maximum
        largest = number
    if number < smallest:                 # Condition for minimum
        smallest = number

print('Maximum is: ',largest)
print ('Minimum is: ', smallest)
