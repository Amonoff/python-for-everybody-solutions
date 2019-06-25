"""
Exercise 5.1: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Amon Ochuka
something easier

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
    if number > largest:                  # Condition for maximum
        largest = number
    if number < smallest:                 # Condition for minimum
        smallest = number

print('Maximum is: ',largest)
print ('Minimum is: ', smallest)
