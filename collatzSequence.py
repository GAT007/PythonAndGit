import sys
def collatzSequence(number):
    try :
        number = int(number)
    except ValueError:
        print("Uh oh! Looks like you haven't given an integer for the value")
        sys.exit()
    while number != 1:
        if number % 2 == 0:
            print("Old number is : " + str(number))
            number = number // 2
            print("New number is : " + str(number))
        elif number % 2 != 0:
            print("Old number is : " + str(number))
            number = 3*number+1
            print("New Number is : " + str(number))

number = raw_input("Enter a number for the sequence : ")
collatzSequence(number)
print ("You just witnessed the Collatz sequence")
