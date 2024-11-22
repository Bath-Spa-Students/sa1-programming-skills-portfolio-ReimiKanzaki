#Is It Even?

def even(number): 
    return number % 2 == 0 
def odd(number): 
    return number % 2 == 1 
def main():
    number= int(input("Please Enter A Number: "))

    if even(number):
        print("The Number", number, "is Even")
    elif odd(number):
        print("The Number", number,"Is Odd")
main()