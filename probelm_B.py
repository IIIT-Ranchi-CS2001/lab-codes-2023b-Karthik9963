from math import *

a=int("enter A:")
b=int("Enter B:")
c=int("Enter C:")

p=(a+b+c)
s=p/2
area=pow((s)*(s-a)*(s-b)*(s-c),1/2)

A=degrees(acos((b*b)+(c*c)-(a*a)/2*b*c))
B=degrees(acos((a*a)+(c*c)-(b*b)/2*a*c))
C=degrees(acos((b*b)+(a*a)-(c*c)/2*b*a))

print("the angles of triangle are",A,B,C)