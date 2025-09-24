
empty_tuple=()
print(empty_tuple)

tup="python","Programming"
print(tup)

tup_1=("python","Programming")
print(tup_1)

int_tuple=(1,2,3)
print(int_tuple)

mixed_tup=(0b101,8,"a",8.8,8+4j,8.e5)
print(mixed_tup)

t = (1, 2, 3, 4)
print(t[0])     # 1
print(t[-1])    # 4


t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)                 # (1, 2, 3, 4)
print(len(t3))            # 4



data = (10, 20, 30)
a, b, c = data
print(a, b, c)


info = ["Alice", 25, "Engineer"]
name, age, job = info
print(name, age, job)


lst = [1, 2, 3, 4]
print(lst[0])     # 1
print(lst[-1])    # 4


lst = [10, 20, 30]
lst[1] = 25           # Update
lst.append(40)        # Add element
lst.remove(10)        # Remove element
print(len(lst))       # 3
#-----------------
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}


my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  


my_dict = {"name": "Alice"}
my_dict["age"] = 25         # Add new key
my_dict["name"] = "Bob"    # Update existing key
print(my_dict)  

my_dict = {"name": "Alice", "age": 25}

print(my_dict.keys())    # dict_keys(['name', 'age'])
print(my_dict.values())  # dict_values(['Alice', 25])
print(my_dict.items())   # dict_items([('name', 'Alice'), ('age', 25)])

def greet(name):
    return f"Hello, {name}!"

pi = 3.14159

