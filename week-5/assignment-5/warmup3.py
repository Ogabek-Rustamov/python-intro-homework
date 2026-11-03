names = ["Alice", "John", "Sarah", "Marcus", "David", "Emma"]

search_name = input("Enter a name to search for: ")

found = False

for index in range(len(names)):
    if names[index].lower() == search_name.lower():
        print(f'Found "{search_name}" at index {index}.')
        found = True
        break

if not found:
    print(f'"{search_name}" was not found in the list.')