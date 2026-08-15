#1
def greet(name, greeting="Hello"):
    print("Hello, " + name + "!")

greet("Alex")

#2
def greet(name, greeting):
    print(greeting + ", " + name + "!")

greet("Alex", "Good morning")

#3
name = "Alex"

def greet(name, greeting):
    print(greeting + ", " + name + "!")

greet(name, "Hello, ")

