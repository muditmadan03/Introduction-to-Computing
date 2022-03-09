#Question 1
print('Question 1')

from tkinter import*
def submit():
    n1 = int(a.get())
    n2 = int(b.get())
    gst=(n2-n1)
    c.set(gst)

root=Tk()
a=StringVar()
b=StringVar()
c=StringVar()
root.title('GST Calculator')
root.geometry('600x600')
lb1=Label(root,text ='Enter Original Cost')
lb1.grid(row=0,column=0)
e1=Entry(root,textvariable=a)
e1.grid(row=0,column=2)
e2=Entry(root,textvariable=b)
e2.grid(row=2,column=2)
lb2=Label(root,text ='Enter Net Price')
lb2.grid(row=2,column=0)
b1=Button(root,text='Submit',command=submit)
b1.grid()
result=Label(root, text="", textvariable=c).grid(row=3,column=1, sticky=W)

root.mainloop()

#Question 2
print('Question 2')
from tkinter import *
import calendar
def submit():
    screen=Tk()
    screen.title('Calendar')
    screen.geometry('600x600')
    l4=Label(screen,text='Calendar',bg='dark grey',font=('times',28,'bold'))
    l4.grid(row=1,column=1)
    screen.config(background='white')
    b=int(a.get())
    year=calendar.calendar(b)
    l3=Label(screen,text=year,font='Consolas 10 bold')
    l3.grid(row=2,column=1,padx=20)
    screen.mainloop()

win=Tk()
win.title('Calendar')
win.geometry('300x300')
a=StringVar()
l1=Label(win,text='Calendar',font=('times',28,'bold'))
l1.grid()
l2=Label(win,text='Enter Year')
l2.grid()
e1=Entry(win,textvariable=a)
e1.grid()
b1=Button(win,text='Submit',command=submit)
b1.grid()
win.mainloop()

#Question 3
print('QUESTION 3')

import tkinter as tk
from tkinter import Label,StringVar,Tk,ttk,messagebox
root = Tk()
root.geometry("600x900")
root.title('Calculator')
i=StringVar()
j=StringVar()
c=StringVar()

def arithmetic():
    print(operation.get())
    if operation.get() == 'Addition':
        n1 = int(i.get())
        n2 = int(j.get())
        f=n1+n2
        print(f)
        c.set(f)
    if operation.get() == 'Division':
        n1 = int(i.get())
        n2 = int(j.get())
        u=n1/n2
        print(u)
        c.set(u)
    if operation.get()=='Subtraction':
        n1 = int(i.get())
        n2 = int(j.get())
        r=n1-n2
        print(r)
        c.set(r)
    if operation.get()=='Multiplication':
        n1 = int(i.get())
        n2 = int(j.get())
        p=n1*n2
        print(p)
        c.set(p)   

root.geometry("600x900")
root.title('Calculator')
lb1=Label(root,text ='Enter number 1')
lb1.grid(row=0,column=0)
e1=tk.Entry(root,textvariable=i)
e1.grid(row=0,column=2)
e2=tk.Entry(root,textvariable=j)
e2.grid(row=2,column=2)
lb2=Label(root,text ='Enter number 2')
lb2.grid(row=2,column=0)
operation = ttk.Combobox(root, width = 27)
lb3=Label(root,text='Choose Arithmetic Operation')
lb3.grid()
operation['values'] = ('Addition','Subtraction','Division','Multiplication')
operation['state'] = 'readonly'
operation.grid()
operation.current(0)
current_operation=operation.get()
b1=tk.Button(root,text='Submit',command=arithmetic)
b1.grid()
l3=Label(root,text='Result')
l3.grid()
result=Label(root, text="", textvariable=c,font=(20))
result.grid()
root.mainloop()






print('Question 4(Using Merge Sort)')
a=list()
b=int(input("Enter marks of student: "))
a.append(b)
while True:
  c=input("Would you like to add marks for more students?")
  if c =="Yes":
    d=int(input('Enter marks of student: '))
    a.append(d)
  elif c =="No":
    print(a)
    break
  else:
    print("Enter Yes/No")
    continue

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  return i + 1
def QuickSort(arr, low, high):
  if low < high:
    pivot = partition(arr, low, high)
    QuickSort(arr, low, pivot - 1)
    QuickSort(arr, pivot + 1, high)
size = len(a)
QuickSort(a, 0, size - 1)
print('The Sorted Array:', a)




print('Question 5')
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
a=list()
b=int(input("Enter marks of student: "))
a.append(b)
while True:
  c=input("Would you like to add marks for more students?")
  if c =="Yes":
    d=int(input('Enter marks of student: '))
    a.append(d)
  elif c =="No":
    print(a)
    break
  else:
    print("Enter Yes/No")
    continue
print('Question 5A')
h=sorted(a)
print('The sorted array is',h)
print('Question 5B')
x=int(input('Enter the element to be searched in the array: '))
result=binary_search(h,0,len(h)-1,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
print('Question 5C')
i=0
j=0
while i<len(h):
  if h[i]==x:
    j+=1
  i+=1
print('The number of occurances of',x, 'is',j)