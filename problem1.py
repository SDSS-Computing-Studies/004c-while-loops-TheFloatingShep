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
Acces denied
"""
user = ""
pas = ""
n = 1
while n <= 3 and (user != "admin" or pas != "12345"):
    user = (input("Input username")).strip()
    pas = (input("Input password")).strip()
    n += 1
    if user != "admin" or pas != "12345":
        print("Access denied")
    else:
        print("Access granted")