print("welcome to simple calculator...")
def add(x,y):     
    return x+y 
def dif(x,y):    
    return x-y 
def prd(x,y):     
    return x*y 
def div(x,y):     
    return x/y   
print("Choose the following operations: ") 
print("1-Addition") 
print("2-Subtraction") 
print("3-Multiplication") 
print("4-Division") 
print("5-Exit")   
while True:  
     opr=float(input("Enter the choice: "))     
     if opr in (1,2,3,4,5):         
        try:  
            num1=float(input("Enter the number 1 : "))             
            num2=float(input("Enter the number 2 : "))         
        except ValueError:              
            print("Invalid input. Please enter a valid input")             
            continue         
        if opr== 1:  
            print(num1,"+",num2,"=",add(num1,num2))         
        elif opr== 2:  
            print(num1,"-",num2,"=",dif(num1,num2))         
        elif opr== 3:  
            print(num1,"*",num2,"=",prd(num1,num2))         
        elif opr== 4:  
            print(num1,"/",num2,"=",div(num1,num2))         
        elif opr== 5:              
            break  
         
        next_calci = input("Want further calculations?(yes/no): ")         
        if next_calci== "no" :              
            break     
else:          
    print("Invalid Input")  


    
  
     
