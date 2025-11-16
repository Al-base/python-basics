"""age4 = int(input("Enter your age : "))
if age4 >=18 and age4 <100:
    print("You are adult")  
elif age4 <0 : 
    print("Invalid age")
elif age4 ==100:
    print("You are centenarian")
else:
    print("You are a child")
temperature = int(input("Enter the temperature : "))
if temperature >30:
    print("It's a hot day")
    print("Drink plenty of water")  
elif temperature >20 and temperature <=30:
    print("It's a nice day")        
elif temperature >10 or temperature <=20:
    print("It's a bit cold")    
elif not(temperature >0 and temperature <=10):
    print("It's cold")
else:
    print("It's freezing cold")"""
"""name = None
while not name:
    name = input("Enter your name : ")
print("Hello "+ name)"""

#for i in range(10):
 #   print(i+1)

#for i in range(5,10+1,2):
 #    print(i)
#for i in "Ali Deeb":
    #print(i)
#for seconds in range(10,0,-1):
 #   print(seconds)
    #time.sleep(1)
#print("Happy New Year!")
#rows = int(input("Enter number of rows : "))
#columns = int(input("Enter number of columns : "))
#symbol = input("Enter a symbol to use : ")  
#for i in range(rows):
   # for j in range(columns):
        #print(symbol , end="")
   # print()

"""while True:
    name = input("Enter your name : ")
    if name != "":
        break
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)  """
#food = ["pizza","hamburger","hotdog","spaghetti","pudding"]
#print(food[0])
#food[0] = "sushi"
#for i in food:
 #   print(i)

#food.append("ice cream")
#food.remove("hotdog")       
#food.pop()    
#food.insert(0,"cake")
#food.sort() 
#food.clear()
#print(food)

"""drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"] 
dessert = ["cake","ice cream"]
food = drinks + dinner + dessert
food = [drinks , dinner , dessert]
for i in food:
    print(i)    
print(food[0][0])"""

"""students = ("Ali",21,"male")
print(students.count("Ali"))
print(students.index(21))   
print(students[0])"""
"""utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}
for i in utensils:
    print(i)

utensils.add("napkin")
dishes.remove("cup")        
utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
for i in utensils:
    print(i)"""
"""capitals = {"USA":"Washington DC",
"India":"New Dehli",    
"China":"Beijing",
"Russia":"Moscow"  
}
print(capitals["India"])
for i in capitals:
    print(i)
    print(capitals[i])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)

capitals.update({"Germany":"Berlin"})
capitals.pop("China")   
capitals.update({"USA":"Las Vegas"})
capitals.clear()    """

"""name = "ali deeb"
if(name[0].islower()):
    name = name.capitalize()
    print("Your name is "+ name)
if name.startswith("a"):
    print("Your name starts with a")"""