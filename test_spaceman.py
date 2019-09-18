from spaceman import is_guess_in_word, is_word_guessed, get_guessed_word
import unittest

class SpaceManTest(unittest.TestCase):
    def test_is_guess_in_word(self):
        """
        This function will test the is_guess_in_word function
           Args:
                secret_word(string)         
           Returns:
                True if letters_guessed is in secret_word
        """
        secret_word = "test"
        self.assertEqual(is_guess_in_word('e',secret_word),True)

    def test_is_word_guessed(self):
        """This test will run using the is_word_guessed function
            Args:
                letters_guessed(string)
                secret_word(string)         
           Returns:
            True if letters are in secret word
        """
        secret_word = ['pillow']
        letters_guessed['p','i','l','l','o','w']
        self.assertEqual(is_word_guessed(secret_word,letters_guessed)True)
    
    def test_get_guessed_word(self):
        """
            This function tests if the letters guessed match all of the secret word itself
            Args:
                secret_word(string)
                letters_guessed(string)
            Return:
                True if the entire word is guessed correctly 
        """
        secret_word = ['tacos']
        letters_guessed['t','a','c','o','s']
        self.assertEqual(get_guessed_word(secret_word,letters_guessed),True)

