print("PYTHON PROGRAMMING IS GOING TO BE STARTED SOON")
Worker1,Worker2,Worker3="Ramesh","Suresh","Mahesh"
print("1st Worker name is",Worker1)
print("2nd Worker name is",Worker2)
print("3rd Worker name is",Worker3)

Worker1_surname=Worker2_surname=Worker3_surname="Kumar"
print("Surname of ",Worker1 ,"is" ,Worker1_surname)
print("Surname of ",Worker2 ,"is" ,Worker2_surname)
print("Surname of ",Worker3 ,"is" ,Worker3_surname)
print("Name of all the workers are",Worker1,Worker2,Worker3)

def myfunc():
    global x
    x="Awesome"
    print(Worker1,"is",x)
myfunc() 

print(x)