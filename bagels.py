"""Have users guess a secret 3 digit number based on clues. The game offers one hint based on your guess. 
'pico' when your guess has a correct digit in the wrong place, 'fermi' when a digit is correct in the correct place, 
'bagels' when none of the digits are correct. The user gets 10 guesses to win"""

from random import randint

def main():
    """The main function that runs the program"""
    # State the rules of the game

    # Generate the secret number
    secret_num = generate_secret_num() #Generates secret number for the program
    # Let user know that you have a number in mind, and that they have 10 guesses to get it right

    # Create loop that asks users to guess secret until theyve guessed 10 times
        # Request user to guess the secret

        # Create a string that keeps track of guess results. 
        # Loop through guess accessing its values and indexes. 
            # Check if guess value is in secret
                # Check if guess value is the same as value at the same index in secret
                    # Concatenate fermi to guess results
                # If not
                    # Concatenate pico to guess results
            # Check if iteration is on last item of guess
                # Check if guess results is empty string
                    # Assign guess results as bagels
                # Else check if guess results fermi fermi fermi
                    # Assign guess results as correct guess

        # Check if guess results is correct guess
            # Tell user they guessed correctly, what their guess was, and what secret was
            # Ask them if theyd like to play again
                # If yes
                    # Run program again
                # Else if no
                    # Close program
        # Else 
            # Tell user their guess was incorrect
            # Tell user their hint
            # Tell them how many guesses they have left.

    # Tell them theyve lost, what the secret was and ask if theyd like to play again

    # If yes 
        # run the main program again
    # If no
        # exit the program

    print(secret_num)


def generate_secret_num():
    """Generates random 3 digit number as a string"""

    # Creates a loop that iterates three times. For each iteration a random integer between 0 and 9 is generated, 
    # coerced to a string, and concatenated to the three_digit_num variable
    three_digit_num = ""
    for num in range(3):
        three_digit_num += str(randint(0, 9))
    
    return three_digit_num

if __name__ == "__main__":
    main()