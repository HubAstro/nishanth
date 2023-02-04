def calculator():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")
        
        choice = int(input("Enter choice(1/2/3/4/0): "))
        
        if choice == 0:
            print("Exiting calculator")
            break
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == 1:
            result = num1 + num2
            print("Result: ", result)
        elif choice == 2:
            result = num1 - num2
            print("Result: ", result)
        elif choice == 3:
            result = num1 * num2
            print("Result: ", result)
        elif choice == 4:
            result = num1 / num2
            print("Result: ", result)
        else:
            print("Invalid input")

calculator()
