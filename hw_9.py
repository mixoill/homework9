contacts = {}  # Словник для зберігання контактів (ім'я - номер телефону)


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Please try again."

    return wrapper


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Added {name} with phone {phone}"


@input_error
def change_phone(command):
    _, name, phone = command.split()
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        raise KeyError


@input_error
def get_phone(command):
    _, name = command.split()
    if name.lower() in contacts:
        return f"Phone for {name}: {contacts[name.lower()]}"
    else:
        raise KeyError


def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available"


def main():
    print("How can I help you?")
    while True:
        command = input("> ").strip().lower()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command.startswith("add"):
            result = add_contact(command)
            print(result)

        elif command.startswith("change"):
            result = change_phone(command)
            print(result)

        elif command.startswith("phone"):
            result = get_phone(command)
            print(result)

        elif command == "show all":
            result = show_all_contacts()
            print(result)

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()



