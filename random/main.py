# Darius Corbin
# PA 6
# Date: 03/10/2023

#minimum random number
#maximum random number
#total of the random numbers
#average random number (use the integer division operation to calculate the average)
#all the random numbers in the list > 50 on a single line separated by a space


import random

# list to store the random integers
random_ints = []

# 20 random integers between 1 and 100
for i in range(20):
    random_int = random.randint(1, 100)
    random_ints.append(random_int)

# random integers
print("Random Number List:", random_ints)

# minimum value
min_value = min(random_ints)
print("Minimum value:", min_value)

# maximum value
max_value = max(random_ints)
print("Maximum value:", max_value)

# sum of the list
list_sum = sum(random_ints)
print("Sum (total) of the list:", list_sum)

# average of the list
list_average = list_sum / len(random_ints)
print("Average random number:", list_average)


# random numbers in the list > 50
greater_than_50 = [num for num in random_ints if num > 50]
print("Random numbers (> 50):", " ".join(str(num) for num in greater_than_50))
