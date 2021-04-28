#single line
"""
print("my name is Arnav")

a=10
print(a)
print(type(a))

a=10.89
print(a)
print(type(a))

a="name"
print(a)
print(type(a))

a=True
print(a)
print(type(a))

a=10+6j
print(a)
print(type(a))

a=[1,2,3,4,5,6,7]
print(a)
print(type(a))

a=(1,2,3,4,4,5)
print(a)
print(type(a))

number=int(input("enter number:"))
print(number)
print(type(number))
"""
"""
num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2:\n"))
add=num1+num2
print("The addition is=",add)
"""
"""
num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2:\n"))
num3=int(input("Enter num2:\n"))
print("before swapping:",num1,num2,num3)

temp=num1
num1=num2
num2=temp

num1=num1+num2+num3
num2=num1-num2-num3
num3=num1-num2-num3
num1=num1-num2-num3

print("after swapping:",num1,num2,num3)

"""
"""
num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2:\n"))
num3=int(input("Enter num3:\n"))
if(num1 > num2 and num1 > num3):
    print("num1 is greater")
elif(num2>num3 and num2>num1):
    print("num2 is greater")
else:
    print("num3 is greater")

"""
"""
# to print multiplicative table of any number

n=int(input("Enter number:\n"))
i=1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i=i+1

n=int(input("Enter number:\n"))
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)
    
"""
"""
a=[1,2,3,4,4,5,6]# list--- collection of data values
print(a)
print(type(a))

for i in a:
    print(i)

a.sort(reverse=True)
print(a)

c=[12,32,43,21,56,34]
print(c)
c.reverse()
print(c)
c.sort()
print(c)
"""
"""
a=input("Enter string:\n")
print(a)
words=a.split(" ")
count=0
for i in words:
    count=count+1
print("Total words=",count)
"""
#function without arguments
"""
def sum():
    a=int(input("Enter a:\n"))
    b=int(input("ENter b:\n"))
    c=a+b
    print(c)

sum()

#function with arguments

def greet(name):
    print("hello",name)

name=input("Enter name:\n")
greet(name)
"""
#file handling:
"""
fp=open("D:/arnav.txt","w")
if fp:
    data =input("Enter input:\n")
    fp.write(data)
    print("written data")
fp.close()
"""
"""
fp=open("D:/arnav.txt","r")
if fp:
    data =fp.read()
    print(data)
    
fp.close()
"""
"""
import random
# return the random integer number
a= random.randint(1,10)
print(a)

#return the random number between 0 and 1
a= random.random()
print(a)

#return the random float values 
a=random.uniform(10,20)
print(a)

# return the random integer number with last value excluded
a= random.randrange(3,10)
print(a)

# return the value from the collection
s=[2,3,5,1,4]
print(random.choice(s))

# returns the randomly re-arranged collection
random.shuffle(s)
print(s)
"""
"""
import os
date=os.system("date")
print(date)

#os.mkdir("D:/Arnav")
print("Folder created successfully")

print(os.getcwd())

path="D:/Arnav"
isExist= os.path.exists(path)
print(isExist)


path="D:/arnav.txt"
root_ext=os.path.splitext(path)
print(root_ext[0])
print(root_ext[1])

print(os.listdir())
"""
"""
import mymodule
name=input("Enter name:\n")
mymodule.greet(name)
"""
"""
import os
import shutil
#copy of content
path1="D:/arnav.txt"
print("before copy:\n")
print(path1)

path2="D:/Arnav/arnav1.txt"

file=shutil.copy(path1, path2)
print("after copy:\n")
print(path2)

#moving of file from one location to another
path1="D:/arnav.txt"
print("before copy:\n")
print(path1)

path2="D:/Arnav/arnav2.txt"

file=shutil.move(path1, path2)
print("after copy:\n")
print(path2)
"""
"""
class Student:
    def __init__(self,name):
        self.name=name
        print("Name:",self.name)

    def message(self):
        print("Hello")

object1=Student("Arnav")
object1.message()
"""
"""
class employee -- constructor you have take company name and printit
class also have one function called as get_details empid and name from the user
and print it
"""

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'HPbWQpIWwqIAAAAAAAAAASmTs8X4DO_jp95oa60GkHKmC0X_KCPdnJ955HGQEdn-'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()

















































































    



































