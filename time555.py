import time
total=time.time()
print(total)
t=0
while(t<40):
    print("this is Raju sir")
    time.sleep(2)
    t+=1
print("while loop ran in:", time.time()-total ,"seconds")
initial=time.time()
for i in range(4):
    print("this is my village parsia")
    i+=1
print("for loop run in:", time.time()-initial, "seconds")
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)