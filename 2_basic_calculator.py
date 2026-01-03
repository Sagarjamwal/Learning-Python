# Input
num1=input("Enter the first operator : \n")
num2=input("Enter the second operator : \n")
op=input("Enter from the following Operators: \t '+','-','*','/'): ")

#Converting the input 
num1=float(num1)
num2=float(num2)

#Loops
if op=='+':
    result=num1+num2
    print(f"The result is {result}")
elif op == '-':
    result=num1-num2
    print(f"The result is {result}")
elif op== '*':
    result=num1*num2
    print(f"The result is {result}")
elif op== '/':
    result=num1/num2
    print(f"The result is {result}")
