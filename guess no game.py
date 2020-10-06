#TRY TO GUESS A NO.
print("guess a number game")
i=0
while(i<8):
    i=i+1
    n=int(input("try to guess the no: \n"))
    if n>18 or n<18:
        print("you entered a wrong no:\n", "no of chances remains:",8-i)
    elif n==18:
        print("you are right")
        break
else:
    print("game is over")
    