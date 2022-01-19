#1st Question
print("1a Question")
a="Python is a case sensitive language"
print(len(a))

print("1b Question")
a="Python is a case sensitive language"
print(a[::-1])

print("1c Question")
a="Python is a case sensitive language"
b=a[10:26]
print (b)

print("1d Question")
a="Python is a case sensitive language"
c= a[:10] + 'object orientated' + a[26:]
print(c)

print("1e Question")
a="Python is a case sensitive language"
print(a.index("a"))

print("1f Question")
a="Python is a case sensitive language"
d=a.replace(" ","")
print(d)



#2nd Question
print("Question 2")
name = "Mudit"
SID = "21105019"
department = "ECE"
CGPA = "9.9"
print(f"Hey, {name.title()} here! \nMy SID is {SID} \nI am from {department} and my CGPA is {CGPA}")




#3rd Question(Bitwise Operators)
print("Question 3(Bitwise Operators)")
a= 56
b= 10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)




#4th Question(Finding greatest of three numbers)
print("Question 4(Finding greatest of three numbers)")
a=float(input("enter number 1="))
b=float(input("enter number 2="))
c=float(input("enter number 3="))

if (a>b) and (a>c):
  print(a)
elif (b>a) and (b>c):
  print(b)
else:
  print(c)




#5th Question(To check if 'name' is present in the string)
print("Question 5(To check if 'name' is present in the string)")
a=input("Enter-") #input string from the user
if 'name' in a:
  print("Yes")
else:
  print("No")




#6th Question(To chech if a triangle can be formed)
print("Question 6(To chech if a triangle can be formed)")
#Taking input of lengths of triangle from the user
a=float(input("Enter length of side 1="))
b=float(input("Enter length of side 2=")) 
c=float(input("Enter length of side 3=")) 

if a<(b+c) and b<(a+c) and c<(a+b):   #Checking the condition of a triangle
  print("Yes")
else:
  print("No")


