import sys, os,datetime

name = input("Enter your name: ")
age = input ("Enter your age: ")
age = int(age)
now = datetime.datetime.now()
age1 = (now.year - age) + 100
print(name + " , you will be 100 years old in  " + str(age1))
