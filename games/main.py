#Darius Corbin
#Guess User's Generation
#12/09/2022


import time

# Define the age ranges for each generation in a dictionary
GENERATION_RANGES = {
    'Gen Z': (0, 27),
    'Millenials': (28, 43),
    'Gen X': (44, 58),
    'Boomers': (59, 77),
    'Silent': (78, 94),
    'Greatest': (95, 109),
}

# Get user input and validate it
while True:
    user_age = input('Enter your age: ')
    if user_age.isdigit():
        user_age = int(user_age)
        break
    else:
        print('Invalid input. Please enter a non-negative integer.')

# Identify which generation the user belongs to
for generation, age_range in GENERATION_RANGES.items():
    if user_age >= age_range[0] and user_age <= age_range[1]:
        print(f'You are a member of the {generation} generation.')
        break
else:
    print('You entered an invalid age.')

time.sleep(10)
