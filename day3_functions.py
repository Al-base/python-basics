def  hello_world(name , last_name , age):
    print("Hello, World!") 
    print("Welcome to Python functions.")
    print("hello  "+ name+" "+ last_name)
    print("You are "+ str(age) + " years old.")
name = "Ali"
last_name = "Deeb"
age = 25
#hello_world(name,last_name, age)

def multiply(a, b):
    return a * b

result = multiply(6 ,8)
#print("The multiplication result is: " + str(result))

def hellouser (name, last_name):
    print("Hello " + name + " " + last_name)

#hellouser(last_name="deeb", name="ALi")

#print(abs(float (input("enter a wholw positive number: "))))
def display_info():
    name = "Alice" # local variable
    print("Name: " + name)

namwe = "Bob" # global variable
#display_info()
#print("Name: " + namwe)

def add_numbers(*args):
    sum_result = 0
    args = list(args)
    args[0] = 100
    for num in args:
        sum_result += num
    return sum_result
sum_result = add_numbers(10, 15,25,30)
#print("The sum is: " + str(sum_result))


def greet_user(**kwargs):
    print("Hello, " + kwargs['first'] + " " + kwargs['last'] + "!")
    print ("hello", end=" ")
    for key, value in kwargs.items():
        print(key + ": " + value , end=" ")

#greet_user(first="John", middle ="Doe" , last="Smith")    
def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
radius = 5
area = circle_area(radius)
#print("The area of the circle with radius " + str(radius) + " is: " + str(area))
def is_even(number):
    if number % 2 == 0 :
        return True
    else:
        return False
num= int(input("Enter a number to check if it's even: "))
 
print("Is " + str(num) + " even? " + str(is_even(num))) 
