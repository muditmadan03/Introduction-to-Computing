#1st Question(Find average of three numbers)
Print ("1st Question(Find average of three numbers)")
a=float(input("enter number 1="))
b=float(input("enter number 2="))
c=float(input("enter number 3="))

print((a+b+c)/3)


#2nd Question(Compute a person's income tax)
Print("2nd Question(Compute a person's income tax)")
a=float(input("Enter Gross Income to the nearest penny=")) #Gross Incom
b=10000 #Standard Deduction
c=int(input("Enter number of dependents=")) #Number of dependents
d=3000 #Dependent Deduction

e=a-b-(c*d) #Taxable Income
Tax=0.02*e

print(Tax)


#3rd Question(Store a student's data in a list)
Print("3rd Question(Store a student's data in a list)")
a=int(input("Enter your SID=")) #SID
b=input("Enter your Name=") #Name
c=input("Enter your Course Name=")#Course Name
d=float(input("Enter your cgpa=")) #CGPA
e=input("Enter your gender F/M/U=") #Gender

list=[a,b,c,d,e]
print(list)


#4th Question(List of marks for 5 students)
Print("4th Question(List of marks for 5 students)")
a=float(input("Enter marks for 1st Student="))
b=float(input("Enter marks for 2nd Student="))
c=float(input("Enter marks for 3rd Student="))
d=float(input("Enter marks for 4th Student="))
e=float(input("Enter marks for 5th Student"))

list=[a,b,c,d,e]
list.sort()
print(list)


#5th Question
Print("5th Question")
color=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
color.pop(3)
print(color)
color.pop(3)
print(color)
color.insert(3,'Purple')
print(color)






