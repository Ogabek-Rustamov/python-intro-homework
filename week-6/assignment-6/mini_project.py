numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    while True:
        swapped = False

        for index in range(len(sorted_numbers) - 1):
            if sorted_numbers[index] > sorted_numbers[index + 1]:
                sorted_numbers[index], sorted_numbers[index + 1] = (
                    sorted_numbers[index + 1],
                    sorted_numbers[index]
                )
                swapped = True

        if not swapped:
            break

    return sorted_numbers


def show_menu():
    print("\nNumber Cruncher")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort numbers")
    print("5. Exit")

    return input("Choose an option: ")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print(f"Minimum: {find_min(numbers)}")

        elif choice == "2":
            print(f"Maximum: {find_max(numbers)}")

        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)

            if index == -1:
                print("Not found")
            else:
                print(f"Found at index {index}")

        elif choice == "4":
            print(f"Sorted numbers: {bubble_sort(numbers)}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


main()