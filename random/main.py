# Darius Corbin
# 03/01/2023
# Fibonacci Sequence

import sys

def fibonacci(n: int) -> int:
    """Return the nth number in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Display a welcome message.
print('''Fibonacci Sequence, by Darius Corbin 

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

# Main program loop.
while True:
    # Keep asking until the user enters valid input.
    while True:
        response = input('Enter the Nth Fibonacci number you wish to calculate (such as 5, 50, 1000, 9999), or QUIT to quit: ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        try:
            nth = int(response)
            if nth < 1:
                raise ValueError("n must be a positive integer.")
            break
        except ValueError:
            print('Please enter a positive integer greater than 0, or QUIT.')

    print()

    # Handle the special cases if the user entered 1 or 2:
    if nth == 1:
        print('0')
        print(f'\nThe #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print(f'\nThe #2 Fibonacci number is 1.')
        continue

    # Display warning if the user entered a large number:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # Calculate the Nth Fibonacci number:
    fib_numbers = [0, 1]
    for i in range(2, nth):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    print(', '.join(map(str, fib_numbers)), end='')
    print(f', {fibonacci(nth)}')
    print(f'\nThe #{nth} Fibonacci number is {fibonacci(nth)}.')

    print()  # Print an empty line for spacing.
