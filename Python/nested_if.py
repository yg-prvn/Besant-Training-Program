a = int(input("Enter a Number 1 : "))
b = int(input("Enter a Number 2 : "))

option = int(input("Enter an Option: \n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n\n"))

if option == 1:
    print("Addtion of Number 1 and 2 is, ", a+b)
elif option == 2:
    print("Substraction of Number 1 and 2 is, ", a-b)
elif option == 3:
    print("Multiplication of Number 1 and 2 is, ", a*b)
elif option == 4:
    print("Division of Number 1 and 2 is, ", a/b)