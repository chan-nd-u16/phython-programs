import random
print("\"hello\"")
print("my name is chandru\nhow about you")
n=input("enter your name:")
a=input("enter your age:")
b=input("enter yr location:")
print(f'so you r {n}')
c=input(f'you r age is {a} and you come from {b} right??')
if(c.lower()=='yes'):
    g=input("done!! can we play a game??")
    if(g.lower()=='yes'):
        print("we can play \"odd or even game\"")
        i = input("instruction:odd or even:??")
        j=int(input("enter a random no 1-10:"))
        num=random.randint(1,10)
        print("now i ll put a number:",num)
        tot=num+j
        print(tot)
        if(((tot)%2==0)):
            if(i.lower()=='even'):
                print(f'{tot} is even  congrats you win')
            else:
                print(f"you chose odd and you lose")
        elif((tot)%2!=0):
            if(i.lower()=='odd'):
                print(f'{tot} is odd congrats you win')
            else:
                print(f'you chose even and you lose')

else:
    print("kidding right nice to meet you")



