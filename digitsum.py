#wap to read no.and display sum of digits.

num=int(input("enter any no."))
s=0
while num!=0:
    n=num%10
    s=s+n
    num//=10
print("sum is :",s)
