n=input("Enter a string:")
t=input("Enter the character which you want to count:")
count=0
for i in n:
    if i==t:
        count +=1
print(count)