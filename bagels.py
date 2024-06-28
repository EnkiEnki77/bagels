"""Have users guess a secret 3 digit number based on clues. The game offers one hint based on your guess. 
'pico' when your guess has a correct digit in the wrong place, 'fermi' when a digit is correct in the correct place, 
'bagels' when none of the digits are correct. The user gets 10 guesses to win"""

from random import randint

def main():
    """The main function that runs the program"""
    
    secret_num = generate_secret_num() #Generates secret number for the program

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