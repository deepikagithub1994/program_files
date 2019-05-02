#wap to count no. of characters, words and lines within string.

str1='''python is
general purpose
programing language'''
cc,wc,lc=0,0,0
for s in str1:
    if s!=' ' or s!='\n':
        cc+=1
    if s==' ':
        wc+=1
    if s=='\n':
        wc+=1
        lc+=1
print("character count=",cc)
print("word count=",wc+1)
print("line count=",lc+1)
