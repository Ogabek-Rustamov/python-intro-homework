number = int(input("Enter a number: "))

# First block: determine the sign.
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Second block: determine whether the number is even or odd.
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
