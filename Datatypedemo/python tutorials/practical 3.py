m1 = int(input("Input marks for python : "))
m2 = int(input("Input marks for java : "))
m3 = int(input("Input marks for daa : "))
m4 = int(input("Input marks for CN : "))
m5 = int(input("Input marks for Toc : "))

sum = m1 + m2 + m3 + m4 + m5 
total = print(sum)

percent = sum/500*100
print("Your percentile is : ",percent)

if(percent>=75):
    print("A")

elif(percent<75 and percent>=65):
    print("B")

elif(percent<65 and percent>=55):
    print("C")

elif(percent<55 and percent>=45):
    print("D")

elif(percent<45 and percent>=35):
    print("E")

elif(percent<=35):
    print("Fail")

else:
    print("Enter marks : ")