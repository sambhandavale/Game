import random
#print("GUESS the Number Game!!!")
x = int(input())
a = random.randrange(1, 7)
if x == a:
    print("CORRECT GUESS!!!")

else:
    print("WRONG GUESS #####")
    print("Number was ",a)
