n=int(input("Enter a number:"))
num=n
sum=0

while(n>0):
    r=n%10
    sum=sum+r
    n=n//10

print(f"the sum of digits of {num} is {sum}")
