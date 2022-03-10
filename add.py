def Addition():
    number1=float(input("Enter first number:\n"))
    number2=float(input("Enter second number:\n"))
    Addition=number1+number2
    
    print(f"The sum is:\n{Addition}")

if __name__ == '__main__':
    print("You are adding!")
    Addition()