def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci
    
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
print(fib(20))




import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'-?d+(.d+)?'
    matches = re.findall(pattern, text)

    for match in matches:
        yield float(match)  

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text))  
    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")




from functools import wraps

contacts = {}

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

def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(item):
    if len(item) !=2:
        raise ValueError
    
    name,phone = item
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(item):
    if len(item) !=2:
        raise ValueError
    
    name, phone = item
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError

@input_error
def show_phone(item):
    if(item) !=1:
        raise ValueError

    name = item[0]
    return contacts.get(name, 'Error: contact not found.')

@input_error
def show_all():
    if not contacts:
        return 'Список контактів порожній!' 
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name} {phone}")
    return '\n'.join(result)

def main():
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
            print(add_contact(item))
        elif command == "change":
            print(change_contact(item))
        elif command == "phone":
            print(show_phone(item))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()







    

