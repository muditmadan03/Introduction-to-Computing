#Question 1
print("1st Question")
a=input("Enter string-").lower()
b=" "
if b in a:  #Counting the occurance of number of words
  def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
  print( word_count(a))
else:      #Counting the occurance of each character in a string
  occr = {}
  for i in a:
    if i in occr:
      occr[i]+=1
    else:
      occr[i]=1 
  print (str(occr))





#Question 2
print("Question 2(Next Date)")
year = int(input("Input a year[1800-2025]: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day =day + 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is %d-%d-%d." % (day, month, year))




#Question 3
print("Question 3")
list=[]

while True:
  b=int(input("enter number-"))
  c=b**2
  list.append((b,c))
  yesorno=input("Add more values(Yes/No)?")
  if yesorno=="No":
    break
  elif yesorno=="Yes":
    continue
  else:
    print('Please enter Yes/No')
    break

print(list)





#Question 4
print("Question 4")
dictionary={10:'A+' and Outstanding Performance' , 9:'A and Excellent Performance',8:'B+ and Very Good Performance' ,7:'B and Good Performance' ,6:'C+ and Average Performance' ,5:'C and Below Average Performance' ,4:'D and Poor Performance'}
i=int(input("Enter grade point of the student-"))
if i in dictionary.keys():
  print("Your grade is",dictionary[i])
else:
  print("Error-Enter a grade point in (4,10)")





#Question 5
print("Question 5")
str = "ABCDEFGHIJK"
i = 0
while 11-i*2 >= 1:
    print(" "*i, str[0 : 11 - i*2])
    i=i+1




#Question 6
print("Question 6")
diction={}

while True:  
  name=input("Enter Student Name-")
  sid=int(input("Enter SID-"))
  diction[sid]=name
  yesorno=input("Do you want to add date of more students(Y/N)?")
  if yesorno=="N":
    break
  elif yesorno=="Y":
    continue
  else:
    print("Please enter Y/N")
    break
print(diction)

print("Question 6B(Sort by Name)")
drry=sorted(diction.items(), key=lambda x:x[1])
ty=dict(drry)
print(ty)

print("Question 6C(Sort by SID)")
lst=sorted(diction.items())
dct=dict(lst)
print(dct)

print("Question 6D(Search for SID)")
a=int(input("Enter SID of student to be searched-"))
if a in diction.keys():
  print(diction[a])
else:
  print ("SID not found")  





#Question 7
print("Question 7")
def Fibonacci_series(Number):
  if(Number == 0):    
    return 0
  elif(Number == 1):
    return 1
  else:
    return (Fibonacci_series(Number - 2) + Fibonacci_series(Number - 1))

n = int(input("Enter the value of 'n': "))
print("Fibonacci Series:", end = ' ')
for n in range(0, n):
  print(Fibonacci_series(n), end=' ')

#Average value of Fibonacci Numbers
#F(1)=0 and F(2)=1
print("Question 7B")
print("Average value of Fibonacci Numbers")
n=int(input("Enter the value for 'n'- "))
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
      return 0
    elif n == 2:
      return 1
    else:
      return Fibonacci(n-1)+Fibonacci(n-2)

i=1
sum=0
while i<=n:
  sum=sum+Fibonacci(i)
  i=i+1

print(sum/n) 





#Question 8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
Integers={1,2,3,4,5,6,7,8,9,10}
#Question8A
print("Question 8A")
set4=(Set1)&(Set2)
set5=(Set1)|(Set2)
print(set5-set4)
#Question8B
print("Question 8B")
set6=Set3|set5
set7=(Set1)&(Set3)
set8=set6-set7-set4
print(set8)
#Question8C
print("Question 8C")
set9=set6-set8
print(set9)
#Question8D
print("Question 8D")
print(Integers-Set1)
#Question8E
print("Question 8E")
print(Integers-set6)


