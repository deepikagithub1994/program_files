#wap to find the given no. amstrong or not.


num=int(input("enter the no."))
copynum=num
s=0
while num!=0:
    n=num%10
    s=s+(n**3)
    num//=10

if s==copynum:
    print(s,"is amstrong")
else:
    print(s,"is not amstrong")
