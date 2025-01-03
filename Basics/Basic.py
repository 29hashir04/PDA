# Basic Python Codes for Parallel and Distributed Computing
# File: basic_codes.py

# Code 1: Simple Calculator
def simple_calculator():
    print("Welcome to the Simple Calculator!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose an operator (+, -, *, /): ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator!"
    return f"Result: {result}"

if __name__ == "__main__":
    print(simple_calculator())

# Code 2: Contact Book Example using List, Dictionary, and Tuple
def contact_book():
    contacts = []
    print("Contact Book")
    while True:
        name = input("Enter contact name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        phone = input("Enter phone number: ")
        contacts.append((name, phone))
        print("Current Contacts:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}")

if __name__ == "__main__":
    contact_book()

# Code 3: Car Class Example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

def main():
    my_car = Car("Toyota", "Corolla", 2020)
    print("Car Information:")
    print(my_car.display_info())

if __name__ == "__main__":
    main()