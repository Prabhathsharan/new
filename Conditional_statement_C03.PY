x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# ------
marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
# ---------
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not a positive number")
----------

is_logged_in = True

if is_logged_in:
    print("Welcome back, user!")
else:
    print("Please log in.")
#------
word = "Python"

for ch in word:
    print(ch)

num = 5

for i in range(1, 11):

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)

numbers = [2, 4, 6, 8]

for num in numbers:
    print("Square of", num, "is", num ** 2)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

words = ["hi", "hello", "hey"]
names = ["Alice", "Bob", "Charlie"]
for w in words:
    for n in names:
        print(w, n)

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()


~                                                                                                                                             
#"for_loops" 48L, 877B

i = 1
while i <= 5:
    print(i)
    i += 1


num = 10
while num > 0:
    print(num, end=" ")
    num -= 2
print()

count = 0
while count < 3:
    name = input("Enter your name: ")
    print("Hello", name)
    count += 1

n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial is:", fact)

secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
print("Correct guess!")
# NESTED
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

i = 5
#"While_loop.py" 77L, 1013B


for i in range(1, 6):
    if i == 3:
        continue
    print(i)



for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd number:", i)


n = 0
while n < 5:
    n += 1
    if n == 2:
        continue
    print("n =", n)



words = ["apple", "", "banana", "cherry", ""]
for word in words:
    if word == "":
        continue
    print("Word:", word)


for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            continue
        print(f"i={i}, j={j}")

~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
#"Continue_Statement.py" 

names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    if name == "Charlie":
        print("Found:", name)
        break
n = 1
while True:
    print("n =", n)
    if n == 5:
        break

  n += 1
for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            break
        print(i, j)



while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Loop stopped")
        break
    print("You entered:", num)


for i in range(1, 10):
    if i == 5:
        break
    print(i)

~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
#"Break_Statements.py" 
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                   
