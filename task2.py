#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username="admin"
password="12345"

while True:
    a=input("username: ")
    if a==username:
        b=input("password: ")
        if b==password:
            break
        else:
            print("Access denied")
    else:
        print("Access denied")

print("Access granted")
    

