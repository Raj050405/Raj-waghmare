num = int(input("Enter no for table: "))
def table(num):
    for x in range(1, 11):
        x = num*x
        print(x)
table(num)