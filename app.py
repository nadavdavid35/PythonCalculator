print("Welcome to our Python calculator")
print("--------------------------------")
result = 0
canPrint = True
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
operand = str(input("Enter an operand: "))

if operand == "+":
    result = n1 + n2
elif operand == "-":
    result = n1 - n2
elif operand == "*":
    result = n1 * n2
elif operand == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        print("Cannot divide by 0")
        canprint = False
elif operand == "a": #a stands for "all" to excecute all the operations
    print(f"{n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {sub}")
    print(f"{n1} * {n2} = {mul}")
    print(f"{n1} / {n2} = {div}")
else:
    print(f"Can't find operand {operand}")
if canPrint == True:
    print(f"Result: {result}")

print("Hello World")
print("Hello people")
