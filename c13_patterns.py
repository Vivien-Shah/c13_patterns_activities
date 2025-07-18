#Write a program to demonstrate a right angle triangle pattern?
'''num=int(input("Enter the number of rows "))
for i in range (num): 
    for j in range(i+1): 
        print("*",end="")
    print()'''
#Write a program to demonstrate a Floyd triangle pattern?
'''num=int(input("Enter the number of rows "))
start=1
for i in range (1,num+1): 
    for j in range(1,i+1): 
        print(start,end=" ")
        start=start+1
    print()'''

#Write a program to demonstrate the numbers in a diamond pattern?
'''row=int(input("Enter the number of rows "))
for i in range (row): 
    for j in range (row-i-1): 
        print(" ",end="")
    for k in range (i+1):
        print("*",end=" ")
    print()
for i in range (row): 
    for j in range (i): 
        print(" ",end="")
    for k in range (row-i):
        print("*",end=" ")
    print()   '''
#Diamond pattern with numbers  
'''row=int(input("Enter the number of rows "))
for i in range (row): 
    for j in range (row-i-1): 
        print(" ",end="")
    start=1
    for k in range (i+1):
        print(start,end=" ")
        start=start+1
    print()
for i in range (row): 
    for j in range (i): 
        print(" ",end="")
    start=1
    for k in range (row-i):
        print(start,end=" ")
        start=start+1
    print()   '''

    


