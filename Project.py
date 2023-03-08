print("** Welcome to Quiz Game! **")
playGame = input("Would You like to play Quiz Game: (Y/N): ")

count = 0

if playGame == 'N':
    print("** Thank You **")
    quit()

print("Let's Play :)")

# Question 1
answer = input("\nWhat is the length of the string 'Hello, World!': ")

if answer == "13":
    count+= 1
    print("Correct!")
    
else:
    
    print("Incorrect!")


# Question 2
answer = input("\nHow many bits are in a byte: ")

if answer == "8":
    count+= 1
    print("Correct!")
    
else:
    
    print("Incorrect!")


# Question 3
answer = input("\nWhat is the maximum value that can be represented by a 16-bit signed integer: ")

if answer == "32767":
    count+= 1
    print("Correct!")
    
else:
    
    print("Incorrect!")

# Question 4
answer = input("\nWhat is the default value of the step parameter in Python's range() function: ")

if answer == "1":
    count+= 1
    print("Correct!")
    
else:
    
    print("Incorrect!")


# Question 5
answer = input("\nHow many comparison operators does Python have: ")

if answer == "4":
    count+= 1
    print("Correct!")
    
else:
    
    print("Incorrect!")


print("\nThanks for playing!!!!\nYou got " + str(count) + " out of 5 question correct.")

