n=input("Enter the string:")
count=0
for i in n:
    if(i.isalnum()):
        count+=1
    else:
        break

if count==len(n):
    print("True")
else:
    print("False")