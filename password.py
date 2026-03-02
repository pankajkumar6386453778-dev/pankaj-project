username = input("enter user name: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("LOGIN Successfully!")
elif (username != "admin"):
    print("wrong username")
else:
    print("Wrong Password")   

       
