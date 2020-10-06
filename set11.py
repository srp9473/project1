s=set()
print(type(s))
l=[1,2,3,4,5]
s1=set(l)
print(s1)
print(type(s1))
s1.add(8)
s1.add(9)
print(s1 )
s1.union({12,13,14})
print(s,s1)
s1=s.intersection({1,2,12})



# s.add(1)
# s.add(2)
# print(s)