# Chatbot

import random

name = input("What's your name? ")
print("Hi there, " + name + ". My name is J0hn, nice to meet you!")


# -----------------How the user feels questions---------------#

def myFeeling(feelings):
    # Choose random number to vary responses
    randresp1 = random.randint(1, 2)
    randresp2 = random.randint(2, 2)
    # Make dictionaries of words that could be used to see how the user is feeling
    goodFeelings = ["happy", "delighted", "great", "okay", "good", "well", "nice"]
    badFeelings = ["sad", "down", "depressed", "unwell", "unhappy", "bad"]

    # If the feeling is good then respond with one of these two responses based on randresp1
    if feelings in goodFeelings:
        # Use randresp1 to see which response to use
        if randresp1 == 1:
            print("That's great to hear!")
        elif randresp1 == 2:
            print("Awesome!")
    # Check if it is a bad feeling
    elif feelings in badFeelings:
        # Use randresp2 to see which response to use
        if randresp2 == 1:
            print("I'm sorry to hear that (；′⌒`)")
            print("\"One day you will tell your story of how you overcame what you went through, ")
            print("and it will be someone else's survival guide.\"")
            print("--Brené Brown")
        if randresp2 == 2:
            print("I'm sorry for you")
            # Take input from user of what's wrong
            wrong = input("What's wrong? \n").lower()
            # Dictionary of things that could mean that nothing is wrong
            nothingWrong = ["nothing", "don't want to share", "It's okay", "nvm", "Never-mind"]
            if wrong in nothingWrong:
                print("Alright, no worries.")
            else:
                print("We don't have to talk about it if you don't want to. \n Let's move on.")
    # If response to feeling is not in the dictionaries then print this and move one
    else:
        print("Alright. Let's continue on.")


# Ask the user how they are feeling
feeling = input("\nHow are you feeling? ").lower()
# run myFeeling function using the input
myFeeling(feeling)


# ------------------Age Question------------------#

def myAge(age):
    # Random response again
    global userAge
    response3 = random.randint(1, 2)

    # If the UserAge is False then check the age
    while not userAge:
        # If the age is under 13 use one of these two responses using response3
        if age < 13:
            if response3 == 1:
                input("You are so young! What are your interests?")
            elif response3 == 2:
                print("That's great that you are still young!")
            # make user age True so it doesn't repeat
            userAge = True
        # If the age is under 18 and greater than or equal to 14 print this response
        elif 14 <= age < 18:
            print("Yeah! You are a teenager! That's crazy!")
            # make user age True so it doesn't repeat
            userAge = True
        # If the age is under 55 and greater than or equal to 18 print this response
        elif 18 <= age < 55:
            print("Oh, cool!")
            # make user age "True" so it doesn't repeat
            userAge = True
        # If the age is under 120 and greater than or equal to 55 print this response
        elif 55 <= age < 120:
            print("So glad to see you here today!")
            # make user age True so it doesn't repeat
            userAge = True
        # If the age is not one of those ages than ask for age again
        else:
            print("You can't be that old. Try again.")
            # Make userAge False to repeat the loop
            userAge = False
            # Ask them again for their age
            age = int(input("What is your age? (Put something in that is reasonable this time) "))


# assign variable user age as False
userAge = False
age_is_int = False
input_age = input("\nWhat is your age? ")
# Check if the age is actually a number and if not make the user input a number again
while not age_is_int:
    try:
        myAge(int(input_age))
        age_is_int = True
    except ValueError:
        print("\nWhoops! That wasn't a whole number")
        input_age = input("\nWhat is your age? (Put a number this time) ")
        age_is_int = False
