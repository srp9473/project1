# a=8
# b=9
# c=sum((a,b))
# print(c)
# def function1(a,b):
#     print("hello this is function 1", a*b)
# function1(7,9)
# function1(2,9)
# function1(12,9)
# function1(11,12)
# function1(1,2)
def function2(a,b):
    """This is the function to calculate the average of two numbers"""
    average=(a+b)/2
    #print(average)
    return average
v=function2(5,7)
print(v)
print(function2.__doc__)