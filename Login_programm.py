# With this programm you can login in your account. 
# Programm checks your usename and password, and if it's right zou will be in. 

username = str(input("Give your username please:")) # User gives his username, 
if username == str("YourUsername"):
    # if username is wrong programm will write: "User not found" (look at the line 15)

    password = str(input("Give your password please: ")) # User gives his password, principe is quite the same, 
    if password == str("YourPassword"):
         # if password is wrong programm will ask to right it one more time (look at the line 12)
        print("Welcome" + str(username) + "!") # If user wrote everything right programm will meet him. 
    else:
        password= str(input("Your password is wrong, please try again:"))
        if password == str("YourPassword"):
            print("Welcome" + str(username) + "!") 
else:
    print("User not found")
        