def division():
    number1=float(input("Enter first number:\n"))
    number2=float(input("Enter second number:\n"))
    quotient=number1/number2
    reminder=number1%number2
    print(f"The quotient is:\n{quotient}")
    print(f"The reminder is:\n{reminder}")
if __name__ == '__main__':
    print("You are dividing!")
    division()