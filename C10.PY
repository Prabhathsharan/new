try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    x = int("abc")
except Exception as e:
    print("Error occurred:", e)


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input, not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    data = [1, 2, 3]
    print(data[5])
except IndexError:
    print("Index out of range!")
except TypeError:
    print("Type error occurred!")



try:
    x = int(input("Enter a number: "))
    print(10 / x)
finally:
    print("This block always executes")


file = None
try:
    file = open("example.txt", "w")
    file.write("Hello World")
finally:
    if file:
        file.close()
    print("File closed")


x = -5
if x < 0:
"exceptions.py" 102L, 1605B