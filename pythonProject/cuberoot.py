a=int(input("enter a number to check both cube root and square root"))
b=a**(1/3)
d=a**(1/2)
if(round(b)**3==a and round(d)**2==a):
    print(f"{a} is a perfect cube and square root")
else:
    print(f"{a}is not a perfect cube and square root")
