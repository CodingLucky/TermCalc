print("Welcome to TermCalc, the Terminal-Based Calculator.")


## Input Types ##
n1 = float(input("First Number: "))
op = input("Which Operator?(+, -, *, /, %): ")
n2 = float(input("Second Number: "))

## Define what to do ##

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    print(n1 / n2)
elif op == "*":
    print(n1 * n2)
elif op == "%":
    print((n1/n2 * 100.0))

else:
    print("Invalid Input, please type a right operator!")
