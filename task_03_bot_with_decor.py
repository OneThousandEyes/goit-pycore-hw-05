from colorama import Fore, Style
from functools import wraps


def input_error(func):
    """Decorator that handles common input-related exceptions and
    returns user-friendly error messages"""
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Please enter correct argument for the command. {Style.RESET_ALL}"
        except KeyError:
            return f"{Fore.RED}Contact not found.{Style.RESET_ALL}"
        except IndexError:
            return f"{Fore.RED}Enter user name.{Style.RESET_ALL}"

    return inner


@input_error
def parse_input(user_input: str):
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts: dict):
    """Add a new contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict):
    """Change an existing contact's phone number."""
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts: dict):
    """Show the phone number of a contact."""
    name = args[0]
    phone = contacts[name]
    return phone


def show_all(contacts: dict):
    """Show all contacts."""
    string_contacts = ""
    for name, phone in contacts.items():
        string_contacts += f"{name}: {phone}\n"
    return string_contacts.strip()


def help_text() -> str:
    """Display usage instructions and examples for invalid commands"""
    return (
        print(
            f"{Fore.RED}\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
            f"!!!!!!!!!!! Invalid command !!!!!!!!!!\n"
            f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{Style.RESET_ALL}\n"
            f"Available commands: {Fore.BLUE}hello, add, change, phone, "
            f"all, close, exit{Style.RESET_ALL}\n"
            f"Examples:\n"
            f"--------------------------------------\n"
            f"{Fore.GREEN}add John 1234567890\n"
            f"change John 0987654321\n"
            f"phone John\n"
            f"all\n"
            f"close{Style.RESET_ALL}\n"
            f"--------------------------------------"
            )
    )


def main():
    """Main function to run the assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            help_text()


if __name__ == "__main__":
    main()
