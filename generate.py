import random
import string
import sys
all_string=string.punctuation+string.ascii_letters+string.digits
no_special_characters=string.ascii_letters+string.digits

def complex():
    c=int(input("ENTER THE COMPLEXITY YOU WANT\n1 FOR HARD\n2 FOR NORMAL(WITHOUT SPECIAL CHARACTERS)"))
    if c>2:
        print("\nPlease appropriate option given\n")
        complex()
    else:
        return c

def generate():
    l=int(input("ENTER THE LENGTH OF PASSWORD YOU WANT\n"))
    complexity=complex()

    password=" "

    if complexity==1:
        for x in range(l):
            password=password+random.choice(all_string)
        return password
    else:
        for x in range(l):
            password=password+random.choice(no_special_characters)
        return password

def again():
    print("\nDO YOU WANT TO GENERATE AGAIN(Y/N) ")
    n=input()

    if n=="y" or n=="Y":
        return True
    else:
        return False



def main():

    p = generate()

    print("GENERATED PASSWORD", p)

    if again():
        main()

    else:

        print("HOPE YOU ARE SATISFIED WITH THE RESULT ,THANK YOU")



print("WELCOME TO PASSWORD GENERATION SIDE\nHERE YOU CAN GENERATE STRONG PASSWORD OF YOUR CHOICE LENGTH\n")
main()



