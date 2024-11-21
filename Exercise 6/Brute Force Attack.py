#Brute Force Attack

Password = "12345"
UserInput = ""
Attempts = 5

while Attempts >0:
    UserInput = input("Enter The Password: ")
    if UserInput == Password:
        print("The Password Is Correct")
        break
    else:
        Attempts = Attempts - 1
        print("The Password Is Incorrect, Try Again. You Have", Attempts, "Attempts Remaining")
        if Attempts == 0:
            print("You Have Reached Maximum Attempts. Try Again Next Time")
