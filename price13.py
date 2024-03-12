"""c = float(input("Enter first number: "))
C = float(input("Enter second number: "))
operation = input("Enter operation (+ for addition, - for subtraction): ")

if operation == '+':
    result = c + C
    
elif operation == '-':
    result = c - C
    print("Result:", result)
elif operation == "*":
    result = c * C
    print("Result:", result)
else:
    print("Invalid operation")
"""
"""def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
"""
"""import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

root = tk.Tk()
root.title('Digital Clock')

label = tk.Label(root, font = ('calibri', 40, 'bold'), background = 'purple', foreground = 'white')
label.pack(anchor = 'center')

time()
root.mainloop()
"""
inp = input("ক :")

print('true') if inp == "k,c" or inp == "y" else print("not")


inp = input("খ :")

print('true') if inp == "kh" or inp == "y" else print("not")

inp = input("গ :")

print('true') if inp == "g" or inp == "y" else print("not")

inp = input("ঘ :")

print('true') if inp == "gh" or inp == "y" else print("not")

inp = input("ঙ :")

print('true') if inp == "ng" or inp == "y" else print("not")

inp = input("চ :")

print('true') if inp == "ch" or inp == "y" else print("not")

inp = input("ছ :")

print('true') if inp == "chh" or inp == "y" else print("not")

inp = input("জ :")

print('true') if inp == "jh" or inp == "y" else print("not")

inp = input("ঞ :")

print('true') if inp == "ng" or inp == "y" else print("not")

inp = input("ট :")

print('true') if inp == "t" or inp == "y" else print("not")

print('true') if inp == "k,c" or inp == "y" else print("not")


inp = input("ঠ :")

print('true') if inp == "th" or inp == "y" else print("not")

inp = input("ড :")

print('true') if inp == "d" or inp == "y" else print("not")

inp = input("ঢ :")

print('true') if inp == "dh" or inp == "y" else print("not")

inp = input("ণ :")

print('true') if inp == "n" or inp == "y" else print("not")

inp = input("ত :")

print('true') if inp == "t" or inp == "y" else print("not")

inp = input("থ :")

print('true') if inp == "th" or inp == "y" else print("not")

inp = input("দ :")

print('true') if inp == "d" or inp == "y" else print("not")

inp = input("ধ :")

print('true') if inp == "dh" or inp == "y" else print("not")

inp = input("ন :")

print('true') if inp == "n" or inp == "y" else print("not")