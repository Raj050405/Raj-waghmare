char="";
word="";
str = str(input("Enter your string : "))
for i in str:
    char=char+i
    if(i==''):
        word=word+1
print(char)
print(word)