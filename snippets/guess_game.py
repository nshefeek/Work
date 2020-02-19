low = high = guess = 50
x = ''

print("Please think of a number between 0 and 100!")
low = high = 0
while x != 'c':

    print("Is your secret number " +str(guess) + " ? : ")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if x == 'h':
        low = guess
        guess += high//2

    elif x == 'l':
        high = guess
        guess -= low//2

    elif x == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print ("Game over. Your secret number was: " +str(guess))

