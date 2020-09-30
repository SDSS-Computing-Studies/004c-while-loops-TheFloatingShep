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
user = ""
pas = ""
while user != "admin" or pas != "12345":
    user = input("Input username\n").strip()
    pas = input("Input password\n").strip()
    if user != "admin" or pas != "12345":
        print("Access denied")
    else:
        print("Access granted")