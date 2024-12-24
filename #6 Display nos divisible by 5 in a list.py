import random
print("This program will display numbers only divisible by 5")

num_x = []

for num in range(5):
    num_x.append(random.randint(0, 100))

print(f"The given list is x: {num_x}")
print("Divisible by 5")

found_divisible_by_5 = False

for num in num_x:
    if num % 5 == 0:
        print(num)
        found_divisible_by_5 = True

if not found_divisible_by_5:
    print("There are no numbers divisible by 5 in the given list")