numbers = [
    42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
    31, 66, 14, 47, 78, 3, 59, 22, 86, 40
]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    # Option 1: Find minimum
    if choice == "1":
        minimum = numbers[0]

        for number in numbers:
            if number < minimum:
                minimum = number

        print(f"The minimum number is {minimum}.")

    # Option 2: Find maximum
    elif choice == "2":
        maximum = numbers[0]

        for number in numbers:
            if number > maximum:
                maximum = number

        print(f"The maximum number is {maximum}.")

    # Option 3: Linear search
    elif choice == "3":
        try:
            search_number = int(input("Enter a number to search for: "))

            found = False

            for index in range(len(numbers)):
                if numbers[index] == search_number:
                    print(f"Found {search_number} at index {index}.")
                    found = True
                    break

            if not found:
                print(f"{search_number} was not found in the list.")

        except ValueError:
            print("Please enter a valid integer.")

    # Option 4: Bubble sort
    elif choice == "4":
        sorted_numbers = numbers.copy()

        while True:
            swapped = False

            for i in range(len(sorted_numbers) - 1):
                if sorted_numbers[i] > sorted_numbers[i + 1]:
                    sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1],sorted_numbers[i]
                    swapped = True

            if not swapped:
                break

        print("Sorted list:", sorted_numbers)

    # Option 5: Quit
    elif choice == "5":
        print("Thanks for using Number Cruncher. Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 5.")