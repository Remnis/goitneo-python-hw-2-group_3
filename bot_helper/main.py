MENU = """
MENU:
# hello : show hello message
# add [name] [phone]: add new Contact
# change [name] [phone]: change Contact number
# phone [name]: show contact phone
# all: show all contacts
# menu: show menu
# exit|close: exit from program
"""


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError,TypeError) as e:
            print(f"{e}")
    return wrapper

def show_menu():
    return MENU

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Add command expect 2 arguments name and phone. Try again")
    name, phone = args
    if len(name) < 3:
        raise ValueError("Name should be more then 3 symbols. Try again")
    if len(phone) < 10:
        raise ValueError("Phone should be more not less 10 symbols. Try again")
    if phone.isdigit() == False:
        raise TypeError("Phone number should include only digits")
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Change command expect 2 arguments name and phone. Try again")
    
    name, phone = args

    if len(phone) < 10:
        raise ValueError("Phone should be more not less 10 symbols. Try again")
    
    if phone.isdigit() == False:
        raise TypeError("Phone number should include only digits")
    
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        return "Contact not found."
    
@input_error
def show_phone(args, contacts):
    (name,) = args
    if name in contacts:
        return contacts.get(name)
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    all_records = ""
    if len(contacts) == 0:
        raise ValueError("There are not contacts in list. Add some new one.")
    for key, value in contacts.items():
        all_records += f"{key}: {value}\n"
    return all_records

@input_error
def show_menu():
    print(MENU)

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    show_menu()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "menu":
            print(show_menu())

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
