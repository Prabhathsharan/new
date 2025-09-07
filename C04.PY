def greet(name):  # name is a parameter
    print("Hello", name)

greet("Alice")    # "Alice" is the argument

def add(x, y):  # x and y are parameters
    return x + y

print(add(5, 3))  # 5 and 3 are arguments


def hello():
    print("Hello World")

hello()



def square(n):
    return n * n

print(square(4))



def greet(name="Guest"):
    print("Welcome", name)

greet()
greet("Bob")


def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))


x = 10  # global

def func():
    x = 5  # local
    print("Inside function:", x)

func()
print("Outside function:", x)


count = 0


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

print(recursive_sum([1, 2, 3, 4, 5]))  


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 3))  


