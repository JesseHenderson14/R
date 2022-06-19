#Jesse Henderson

#setting favorite model name
vacname = 'madhare'

#marker variable for guess count
guess_count = 1

#guess variable
user_guess = ''

#keeps the while running while true
active = True

while active:
    user_guess = input("Guess the model name I chose > ") #asking for a user guess for my fav model
    if guess_count == 3 and user_guess.lower() != vacname.lower(): #if the guess count is 3 and the userguess does not equal my fav model the program ends
        print("\nYou ran out of guesses, it's okay though.")
        active = False #shuts off while loop ends program
    if user_guess.lower() != vacname.lower(): #if the user guess does not equal my fav model
        print("\n\t•Incorrect, you have", 3-guess_count,"guesses left") #this prints how many guesses are left based on the amount of current guesses from the guess count variable
        guess_count += 1 #marker for guess count variable
        
    elif user_guess.lower() == vacname.lower(): #if the user guesses the correct model 
        print("\nThat's right, good guess!") 
        print("\n\t•This took you",guess_count,"try(s).") #prints the amount of guesses it took to correctly guess the fav model
        guess_count += 1 #marker for guess count variable
        active = False #shuts off while loop ends program
    
    

