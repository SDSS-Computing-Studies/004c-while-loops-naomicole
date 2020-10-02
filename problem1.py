##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""

username="admin"
password="12345"
c=0
c=int(c)

while c<3:
 a=input("username: ").strip()
 b=input("password: ").strip()
 if a==username and b==password:
     print("Access granted")
     break
 else:
     print("Access denied")
     c=c+1
     c=int(c)
    
