#Simple Search

names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

print("Guess Who We're Looking For!")

print(names)
Guess = str(input("Who Do You Think We're Looking For?: "))
if Guess == "Sam":
    print("Correct!")
else:
    print("Wrong! Try Again!")