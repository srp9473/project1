def das(normal , *args ,**kwargs):
    print(normal)
    for item in args:
         print(item)
    print("now i like to introduced some heros:")
    for key, value in kwargs.items():
     print(f"{key} is a {value}")
kw={"satish":"programmer", "rohan":"coock", "ratan":"monitor"}

sat=("satish","rohan","aman","renu","mom")
normal=("this is normal argument and name of students:")
das(normal,*sat,**kw)