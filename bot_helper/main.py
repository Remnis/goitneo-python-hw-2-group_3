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


def show_menu():
    return MENU


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    (name,) = args
    if name in contacts:
        return contacts.get(name)
    else:
        return "Contact not found."


def show_all(contacts):
    all_records = ""

    for key, value in contacts.items():
        all_records += f"{key}: {value}\n"
    return all_records

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
