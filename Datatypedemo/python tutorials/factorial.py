def fact(num):
    if(num<1):
        print("error")
    else:
        x = 1
        for y in range(1,num+1):
            x= x*y
        print(x)
fact(4)
