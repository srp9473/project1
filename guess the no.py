# n=12
# i=9
# while i<=9:
#     print("you have left no of chances:", i-1)
#     i=i+1
#     g=int(input("guess the no:"))
#     if g<n:
#         print("you entered lesser no")
#     elif g>n:
#         print("you entered greater no")
#     elif g==n:
#         print("you are right")
#         break
# if i>9:
#     print("game is over you loose this game")
#     i=i+1

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