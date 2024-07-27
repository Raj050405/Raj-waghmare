def greatest_of_two(x,y):
    if (x>y):
        return x
    return y
print(greatest_of_two(5,9))

def greatest_of_three(x,y,z):
    return (x,(greatest_of_two(x,greatest_of_two(y,z))))
print(greatest_of_three(3,5,9))
