#wap to print character except vowel.

str=input("enter any string")
for c in str:
    if c in "aeiou":
        continue
    print(c)
