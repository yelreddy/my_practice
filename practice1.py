
# Program to Compare two Lists


lst1=[10,20,30,'krupa', 'amazon', 'iisc','zerodha']
lst2=[40,50,20,60,'iit', 'iisc', 'google', 'spacex', 'zerodha']

for i in lst1:
    for j in lst2:
        if i==j:
            print("the Common element is " , i)

# Program to Check odd even and Compute Squares
for i in range(21):
    if (i%2) !=0:
        print(i)
    elif i%2 ==0:
        print(i**2)


