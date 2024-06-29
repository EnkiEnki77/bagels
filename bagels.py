"""Have users guess a secret 3 digit number based on clues. The game offers one hint based on your guess. 
'pico' when your guess has a correct digit in the wrong place, 'fermi' when a digit is correct in the correct place, 
'bagels' when none of the digits are correct. The user gets 10 guesses to win"""

from random import randint

def main():
    """The main function that runs the program"""
    # State the rules of the game
    print("""Rules:
  I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.""")

    # Create loop that allows the game to restart
    while True:
        # Generate the secret number
        secret_num = generate_secret_num() #Generates secret number for the program
        # Let user know that you have a number in mind, and that they have 10 guesses to get it right
        print("\nIve thought up a number.")
        print("You have ten guesses.")

        # Create an empty string that keeps track of guess results. 
        guess_results = ''
        # Create loop that asks users to guess secret until theyve guessed 10 times
        for guess_num in range(10):
            # Request user to guess the secret
            print(f"\nSecret num is: {secret_num}")
            guess = input("What's your guess?(3-digit number): ")

            # Loop through guess accessing its values and indexes. 
            for i, val in enumerate(guess):
                # Check if guess value is in secret
                if val in secret_num:
                    # Check if guess value is the same as value at the same index in secret
                    if val == secret_num[i]:
                        # Concatenate fermi to guess results
                        guess_results += 'fermi '
                    # If not
                    else:
                        # Concatenate pico to guess results
                        guess_results += 'pico '
                # Check if iteration is on last item of guess
                if i == len(guess) - 1:
                    # Check if guess results is empty string
                    if guess_results == '':
                        # Assign guess results as bagels
                        guess_results = 'bagels'
                    # Else check if guess results fermi fermi fermi
                    if guess_results.rstrip() == 'fermi fermi fermi':
                        # Assign guess results as correct guess
                        guess_results = 'correct'

            print(f"Guess results: {guess_results}")
            # Check if guess results is correct guess
            if guess_results == 'correct':
                # Tell user they guessed correctly, what their guess was, and what secret was
                print(f"\nYour guess was: {guess}, and the secret number was: {secret_num}")
                print("You win!")
                # Ask them if theyd like to play again
                answer = input("Would you like to play again?(yes/no) ")
                # If yes
                
                if answer == 'yes':
                    print(answer)
                    # Run program again
                    break
                # Else if no
                elif answer == 'no':
                    # Close program
                    return      
            # Else 
            else:
                # Tell user their guess was incorrect
                print(f"\n{guess} is incorrect")
                # Tell user their hint
                if guess_num + 1 < 10:
                    print(f"Your guess hint is: {guess_results}")
                # Tell them how many guesses they have left.
                guess_results = ''
                print(f"This was guess number {guess_num + 1}.")

        # Tell them theyve lost, what the secret was and ask if theyd like to play again
        if guess_results != 'correct':
            print(f"Youve lost! The secret was {secret_num}")
            answer = input("Would you like to play again?(yes/no)")
            # If yes 
            if answer == 'yes':
                # run the main program again
                continue
            # If no
            elif answer == 'no':
                # exit the program
                break 



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