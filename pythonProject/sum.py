a=(input("enter two digit number:"))
b=(input("enter another number"))
c=len(a)
d=len(b)
sum=int(a)+int(b)
if(d<=2&c<=2):
    print(f"the sum of {a} and {b} is{sum} ")
else:
    print("2 digit number only allowed\nyou entered more than 2 digit")