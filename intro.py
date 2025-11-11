import math
print("ali")
Firat_name ="Ali"
Last_name = "Deeb"
Full_name = Firat_name +' '+ Last_name
print("Hello "+ Full_name)
print(type(Full_name))
Age = 29
Age = Age+1
print(Age)
Age+=1
print(Age)
print(type(Age))
print("Your Age is = "+ str(Age))
Height = 176.5
print(Height)
print(type(Height))
print("Your height is :"+ str(Height)+"CM")
Human = True
print(Human)
print(type(Human))
print("are you a human : "+str(Human))
Name,age2,Atrractive = "Ali" , 21 , True
personA = personb =personec = 30
print(personA)
print(personb)
print(personec)
print(len(Name))
print(Name.find("l"))
print(Name.capitalize())
print(Name.upper())
print(Name.lower())
print(Name.isdigit())
print(Name.isalpha())
print(Name.count("A"))
print(Name.replace("A","M"))
print(Name*3)
x = 1 #int
y = 2.0 #float
z = "3" #str
z = int(z)
x = float(x) 
print(x)
print(str(y))
print(z*3)
#name3 = input("What is your name ? ")
#age3 = input("How old are you ? ")
#Height3 = float(input("What is your height ? "))
#print("Your height is "+ str(Height3))
#print("Hello "+ name3 + " Your age is "+ age3)
pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(-pi))   
print(pow(pi,3))
print(math.sqrt(36))
A4 = 5
B4 = 3  
c4 = A4 + B4
print(max(A4,c4))
print(min(A4,B4))
Unsliced_name = "ALI DEEB"
First_Sliced_name = Unsliced_name[0:3]
print(First_Sliced_name)
Second_Sliced_name = Unsliced_name[4:8]
print(Second_Sliced_name)
Third_Sliced_name = Unsliced_name[::2]
print(Third_Sliced_name)
reversed_name = Unsliced_name[::-1]
print(reversed_name)
Fourth_Sliced_name = Unsliced_name[-4:]
print(Fourth_Sliced_name)
Fifth_Sliced_name = Unsliced_name[:-4]
print(Fifth_Sliced_name)
website = "http://www.abc.com"
slice = slice(7,-4)
sliced_website = website[slice]
print(sliced_website)
age4 = int(input("Enter your age : "))
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
elif temperature >20 or temperature <=30:
    print("It's a bit cold")    
elif not(temperature >0 and temperature <=10):
    print("It's cold")
else:
    print("It's freezing cold")