import random
letters_guessed = []
# given_guesses = 7

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    word = []
    for letter in secret_word:
        if letter in letters_guessed:
            word.append(letter)

    return secret_word == word

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    word = []
    
    for letter in range(len(secret_word)):
        word.append('_')
    
    for letter in secret_word:
        if letter in letters_guessed:
            word[secret_word.index(letter)] = word[secret_word.index(letter)]
    
    return ''join(word)

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    secret_word = list(secret_word)

    return guess in secret_word

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec
    print("Input a letter, if you choose right, keep guessing until you complete the game. If you choose incorrectly a spaceman will be lost to space")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    guesses = 7
    while  given_guesses != 0:
        user_guess = input('Enter one letter only: ')
        
        letters_guessed.append(letters_guessed)

        if (is_guess_in_word(secret_word,letters_guessed)):
            print f'{user_guess} was found! Nice job!'
            print(get_guessed_word(secret_word,letters_guessed))
        else:
            print(get_guessed_word(secret_word,letters_guessed))
            given_guesses -= 1
            print f'You have {given_guesses} remaining. You got this!'
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        is_guess_in_word(user_guess, secret_word)

    #TODO: show the guessed word so far
    get_guessed_word(secret_word,letters_guessed)
    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)