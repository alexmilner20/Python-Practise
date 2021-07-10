def times():
    print("Welcome to the Calculator")
    print("Please just insert numbers, dont do this '100,000'")
    math = input("What is the math type:")
    firstNumber = input("What is your first number:")
    secondNumber = input("What is your second number:")
    floatFirst = int(firstNumber)
    floatSecond = int(secondNumber)

#See if the input contains the mathematical methodology then act depending on the input.
    if math == "times":
        print(floatFirst * floatSecond)
    elif math == "divide":
        print(floatFirst / floatSecond)
    elif math == "add":
        print(floatFirst + floatSecond)
    elif math == "subtract":
        print(floatFirst - floatSecond)
    else:
        print("Invalid Math Type")


times()
