try:
    with open("../data/missing.txt", "r") as file:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')
