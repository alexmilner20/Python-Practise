def incometax():
    gi = input("Gross Income: ")

    if float(gi) <= 12500:
        print("You don't pay any taxes")
    elif 50000 > float(gi) >= 12501:
        tax = (float(gi) - 12500) * 0.2
        print(f"You pay £{tax} in taxes")
    elif 150000 > float(gi) >= 50001:
        tax = (float(gi) - 12500) * 0.4
        print(f"You pay £{tax} in taxes")
    else:
        tax = (float(gi) - 12500) * 0.45
        print(f"You pay £{tax} in taxes")


calc = input("What type of tax is it:")

if calc == "income":
    incometax()
