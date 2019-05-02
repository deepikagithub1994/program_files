#wap to capitalize string without using predefined method.


str1=input("input any string :")
str2=str()
for s in str1:
    o=ord(s)
    if(o>=97 and o<=122)and str2=='':
        o=o-32
        c=chr(o)
        str2=str2+c
    elif (o>=65 and o<=91) and str2=='':
        c=chr(o)
        str2=str2+c
    elif o>=65 and o<=91:
        o=o+32
        c=chr(o)
        str2=str2+c
    else:
        str2=str2+s
print(str1)
print(str2)
