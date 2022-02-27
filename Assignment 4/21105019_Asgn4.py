#Question 1
print("Question 1")
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
TowerOfHanoi(3,'A','B','C')
# A, C, B are the name of rods



print('Question 2(Pascal Triangle)')
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
n = int(input('Enter number of lines for pascal triangle:'))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()



print("Question 2(Method 2)")
n = int(input('Enter Number: '))
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    C = 1
    for j in range(1, i+1):
 
        print(' ', C, sep='', end='')
 
        C = C * (i - j) // j
    print()




print("Question 3(Using Built-In Functions)")
a=int(input("Enter number 1= "))
b=int(input("Enter number 2= "))
c=divmod(a,b)
print(f"The quotient obtained is {c[0]} and remainder is {c[1]}")
print("Question 3A")
g=callable(divmod(a,b))
if g is True:
  print("Callable")
elif g is False:
  print('Not-Callable')
print("Question 3B")
list1=list()
list1.append(c[0])
list1.append(c[1])
d=0
if d in list1:
  print("All values are not Non Zeros")
else:
  print("All values are Non Zeros")
print("Question 3C")
list1.append(4)
list1.append(5)
list1.append(6)
print('After adding (4,5,6) to the result')
print(list1)
list2=list()
for i in range(0,5):
  if list1[i]>4:
    list2.append(list1[i])
print('Filtering out values greater than 4')
print(list2)
print('Question 3D')
print(set(list2))
print('Question 3E')
frozenset(set(list2))
print("The above set has been converted to immutable.")
print("Question 3F")
f=max(set(list2))
print(f"The maximum value is {f}")
print(f"The hash value of {f} is ",hash(f) )



print("Question 4(Name and Roll Numbers of Students)")
class Student:
  def __init__(self,name,rollnumber):
    self.name=name
    self.rollnumber=rollnumber
  def __del__(self):
    print("Object destroyed")
  def disDetails(self):
    print("Name:",self.name, ", Roll Number:",self.rollnumber)

s1=Student("Ram",23)
s1.disDetails()
del s1




#Question5
print("Question 5(Employees and their salaries)")
class Employee:
  count=0
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.count+=1
  def disCount(self):
    print(f"There are {Employee.count} employees")
  def disDetails(self):
    print("Name:",self.name, ", Salary:",self.salary)
Mehak=Employee("Mehak",40000)
Ashok=Employee("Ashok",50000)
Viren=Employee("Viren",60000)

Viren.disCount()
Mehak.disDetails()
Ashok.disDetails()
Viren.disDetails()

print("Question 5A")
Mehak.salary=70000
Mehak.disDetails()
Ashok.disDetails()
Viren.disDetails()

print("Question 5B")
Mehak.disDetails()
Ashok.disDetails()
del Viren
print("Record of Employee Viren is deleted")




print("Question 6(Friendship Test)")
a="George"
b="Barbie"

c=input(f"Enter word for {a}: ")
d=input(f"Enter word for {b}: ")
e=c.lower()
f=d.lower()
def check():
  if (sorted(e)== sorted(f)):
    print(f"Friendship of {a} and {b} is Real!!")
  else:
    print(f"Friendship of {a} and {b} is Fake")

check()