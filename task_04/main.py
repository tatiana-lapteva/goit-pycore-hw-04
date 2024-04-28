"""
Bot-helper, works with user contacts
"""

from parse import parse_input, parse_args
from contacts import add_contact, change_contact, show_phone


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:").strip().lower()
        command, *args = parse_input(user_input)
        name, phone = parse_args(args)
        
        if command in ["close", "exit"]:

            print("Good Bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result, contacts = add_contact(name, phone, contacts)
            print(result)
    
        elif command == "change":
            result, contacts = change_contact(name, phone, contacts)
            print(result)
        
        elif command == "phone":
            print(show_phone(name, contacts))
           
        elif command == "all":
            print(contacts)
        
        else:
            print("Invalid command.")
    
    
    
  
if __name__ == "__main__":
    main()


