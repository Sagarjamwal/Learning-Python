# Just a plain calculator using functions instead
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Welcome to the Calculator!:")
print("Select the Operations from the following:1,2,3,4")
print("1.Add \t 2.Subtract \t 3.Multiply \t 4.Divide ")

choice=input("Enter the choice 1/2/3/4:")
x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))

if choice=='1':
    result=add(x,y)
    print(f"The Addition of {x},{y} is {result}")
elif choice=='2':
    result=subtract(x,y)
    print(f"The Subtraction of {x},{y} is {result} ")
elif choice=='3':
    result=multiply(x,y)
    print(f"The Multiplication of {x},{y}is {result}")
elif choice=='4':
    result=divide(x,y)
    print(f"The Division of {x},{y} is {result}")
else:
    print("Invalid Input")

