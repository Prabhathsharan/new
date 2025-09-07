# Open a file in write mode
file = open("example.txt", "w")

# Write data to the file
file.write("Hello, this is a file operation example.\n")

# Always close the file
file.close()


# Open file in read mode
file = open("example.txt", "r")

# Read the entire content
content = file.read()
print(content)

# Close the file
file.close()

with open("example.txt", "a") as file:
    file.write("Appending another line.\n")

with open("example.txt", "r") as file:
    print(file.read())