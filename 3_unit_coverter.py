#function introduction
def kms_to_miles(kms):
    miles= kms * 0.621371
    return miles # return is added so that value is not thrown into garbage

def celsius_to_fahrenheit(cel):
    f=(cel * 9/5)+32
    return f

print("This is a basic unit converter that converts: \n 1: Kilometers to Miles\n 2:Celsius to Fahrenheit")
choice=float(input("Enter the desired conversion from the menu: "))
if choice == 1:
        value=float(input("Enter the Distance in Kilometers : "))
        result=kms_to_miles(value)
        print(f"{value}km in miles are {result:.2f}") #:.2f tells to format upto 2 decimal places
elif choice ==2:
        value=float(input("Enter the Temperature in Celsius: "))
        result=celsius_to_fahrenheit(value)
        print(f"The Temperature {value} in Fahrenheit is {result:.2f}")
else:
        print(f"Invalid Input")
    

    