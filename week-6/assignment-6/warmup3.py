def create_message():
    message = "Hello from inside the function"


create_message()

# print(message)
# NameError: name 'message' is not defined


def get_message():
    message = "Hello from inside the function"
    return message


message = get_message()
print(message)