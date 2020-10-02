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
    a=input("username: ").strip()
    b=input("password: ").strip()
    if a==username and b==password:
     break
    else:
        print("Access denied")

print("Access granted")
    

