#! /home/user/anaconda2/envs/bioinf/bin/python

#Q1: Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console.
#Using a for loop
x = 0
print(x)
for i in range (100): #CK: Using a range of 100 is wasteful -1
    if i<=4:
        i+=1
        print(i)
print("Done")
#Using a while loop
i = 0
while i <= 5:
    print(i)
    i = i+1
print('Done')

#Q2: Repeat the previous problem, but the loop will skip printing x = 5 to the console but will print values of x from 6 to 10

x = 0
for i in range (100): #CK Same here, you are not using range correctly 
    if i !=5 and i<=10:
        print(i)
print("Done")

#Q3: Create a for loop that prints values from 4 to 10 to the console -1


x = 0
for i in range(100): # CK:  -1
    if i>=3 and i<10:
        i +=1
        print(i)
print("Done")
