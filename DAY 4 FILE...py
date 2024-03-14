++'''----------> DAY 4

#------> while loop
# ------> break  using while loop


# eg:1
# 1.)Iterate from 20 to 30 and break the loop in 27

 i = 20
 while i<31:
     if i ==27:
         break
        print(i)
        i+=1

# 2.)        
   i = 20
 while i<31:
     if i ==27:
      print(i)
         break
      i+=1  

# ! ------> conitinue

# ---> Eg:1

  i = 20
 while i<31:      
     if i ==27:
          contiue
        print(i)
        i=i+1


 i = 20       
 while i<31:
     i=i+1
     if i ==27:
         contiue
        print(i)
        


# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

 i = 12
  sum=0
 while i<23:
     
     sum=sum+i
   print(sum)
   i+=1
# print(sum)

# ! Eg:6
# Find the average of value from 20 to 25

i = 20
sum = 0
count = 0
while i<=30:
     sum=sum+i
     count+=1
     i+=1
print(sum/count)


# ! ------> Nested for loop
# Eg:1

 for row in range(1, 3):
 for col in range(1, 4)+1):
    print(row,col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

 rows = int(input("enter the rows:"))
 cols = int(input("enter the cols:"))
 
for col in range(4):
    for col in range(cols):
  print("*",end="")
 print()
'''
# sum = 0
for row in range(5):
   for col in range(5):
       sum= sum+1
    print(row ,end="")
 print()


 # ! to print stars in right angled triangle




 for row in range(0,6):
     for col in range(0,row+1):
         print("*", end="")
      print()


# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for row in range(6,0,- 1):
    for col in range(0,row):
        print("*",end= "")
     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

##
     *
   * * *
  * * * *
 * * * * *  


# for row in range (0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or
                                                                     (row==2 and (col>=1 and col<=5))):
            print("*",end="")
          else:
              print("", end="")
       print()


# -------> list


# -------> Data types
# Primary


# Number --> int,float complex
# string
# boolean
# None

# Collection
# List
# tuple
# set
# dictionary


# ? ---> List

1.) if the collection of elements are surrounded by by square brackets,it is cosiderd
    to be list
# ! eg:
     # 11= [4, 7, 9, 9.89, "hello", 7+9],[8, 9,0]]


# charactristics of list
  1.) List have to be sorrounded by []
  2.) It is mutable (the elements in list are changable)
  3.) Every element inside list is indexed
  4.) The elements inside list will be orderderd format
  5.) It can hold duplicate values
  6.) Its heterogenous

'''
# To access the elements in list
  lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
   print(lst1)

   -----> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with pre-defined unique value called index value

# We have 2 types of indexing
# Positive indexing---->starts with 0 from left hand side
#Negative indexing-----> starts with -1 from right hand side


# ? --> positive indexing
# list = [1, 4, 1, 7,7.5,"p", "i"]
# print(lst1[0])
# print(lst1[4])
# print(lst1[20])-->error


# ? -----> Negative indexing
# lst = [1,4, 1, 7,89.7,7.5,"P","i"]
  print(lst1[-1])
   print(lst1[-5])
'''
# ? ------> slicing
  lst = [1,4, 1, 7,89.7,7.5,"P","i"]
  lst1[starts_index:end_index:step)
  
  print(1st1[0:4]       
  print(1st1[6:8]
  print(1st1[3:6]   
  print(1st1[:5])
  print(1st1[3:])
  print(1st1[:])


 print(1st1[0:7:1]) # lst1[0:7] --> both are same
 print(1st1[0:7:2])

# trail = int(input())


 lst = [1,4, 1, 7,89.7,7.5,"P","i"]         

  print(1st1[-4:-1]   
  print(1st1[-1:-4])--->[]
  print(1st1[-7:-1])
  print(1st1[-7:-1:2])


# ! To insert  to add element inside list

# append() --> used to add element at last position of list
# lst1 = [9, 8, 0, 6]
# lst1.append("car")
   print(lst1)


 
