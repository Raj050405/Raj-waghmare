print("Enter your choice for calculte the values\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Exit\n")
calculate = int(input("Enter your according the list : "))
if calculate>=5:
    print("Enter a valid choice : ")
num1 = int(input("Enter 1 number : "))
num2 = int(input("Enter 2 number : "))
if calculate==1:
    print(num1 + num2)
elif calculate==2:
    print(num1 - num2)
elif calculate==3:
    print(num1 / num2)
elif calculate==4:
    print(num1 * num2)
else:
    print("exit")