from functools import wraps


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'Error: contact not found.'
        except IndexError:
            return 'Error: please provide the necessary arguments'
        
    return inner

@input_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(item, contacts):
   
    name,phone = item
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(item, contacts):
    
    name, phone = item
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError

@input_error
def show_phone(item, contacts):

    name = item[0]
    return contacts.get(name, 'Error: contact not found.')

@input_error
def show_all(contacts):
    if not contacts:
        return 'Список контактів порожній!' 
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name} {phone}")
    return '\n'.join(result)

def main():
    contacts = {}
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, item = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(item, contacts))
        elif command == "change":
            print(change_contact(item, contacts))
        elif command == "phone":
            print(show_phone(item, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()







    

