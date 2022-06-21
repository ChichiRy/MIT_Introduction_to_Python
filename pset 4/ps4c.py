# Problem Set 4C
# Name: Ryan Chironga <Chichi_Ry>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations
from ps4b import CiphertextMessage
from ps4b import get_story_string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        # pass #delete this line and replace with your code here
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        # pass #delete this line and replace with your code here
        valid_words = self.valid_words.copy()
        return valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        encryption_dict = {}
        lower_vowels_permutation = list(vowels_permutation)
        upper_vowels_permutation = list(str.upper(vowels_permutation))
        index_upper = 0
        index_lower = 0
        
        for letter in string.ascii_letters:
            if letter in CONSONANTS_LOWER:
                encryption_dict[letter] = letter
            elif letter in CONSONANTS_UPPER:
                encryption_dict[letter] = letter
            elif letter in VOWELS_LOWER:
                encryption_dict[letter] = lower_vowels_permutation[index_lower]
                index_lower += 1
            elif letter in VOWELS_UPPER:
                encryption_dict[letter] = upper_vowels_permutation[index_upper]
                index_upper += 1
        return encryption_dict
        # pass #delete this line and replace with your code here

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''    
        # pass #delete this line and replace with your code here
        message_text = SubMessage.get_message_text(self).split(' ')
        encrypted_text = []
        for word in message_text:
            word = list(word)
            encrypted_word = []
            for character in word:
                if character in string.ascii_letters:
                    encrypted_word.append(transpose_dict[character])
                else:
                    encrypted_word.append(character)
            encrypted_word = ''.join(encrypted_word)
            encrypted_text.append(encrypted_word)
        encrypted_text = ' '.join(encrypted_text)
        return encrypted_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # pass #delete this line and replace with your code here
        encrypted_message = self.get_message_text()
        possible_vowel_permutations = get_permutations(VOWELS_LOWER)
        correct_words = (0, 100000000000000000000)
        for permutation in possible_vowel_permutations:
            transpose_dict = self.build_transpose_dict(permutation)
            decrypted_message = self.apply_transpose(transpose_dict)
            decrypted_message = decrypted_message.split(' ')
            word_count = len(decrypted_message)
            for word in decrypted_message:
                word_list = self.get_valid_words()
                if is_word(word_list, word):
                    word_count -= 1
                else:
                    {}
            # only considering all words are in dictionary
            if word_count == 0:
                decrypted_message = ' '.join(decrypted_message)
                return decrypted_message
            else:
                if correct_words[1] >= word_count:
                    correct_words = (permutation, word_count)
                else:
                    {}

        if correct_words[1] > 0:
            transpose_dict = self.build_transpose_dict(correct_words[0])
            decrypted_message = self.apply_transpose(transpose_dict)
            return decrypted_message
        else:
            return encrypted_message

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    #TODO: WRITE YOUR TEST CASES HERE
    
    story = get_story_string()    
    ciphertext_2 = CiphertextMessage(story)
    ciphertext_2 = ciphertext_2.decrypt_message()
    message = SubMessage(ciphertext_2)
    permutation = 'iaueo'
    enc_dict = message.build_transpose_dict(permutation)
    # print('Original message: ', message.get_message_text(), 'Permutation:', permutation)
    # print('Encrypted message:', message.apply_transpose(enc_dict))
    print('Decrypted Message:', EncryptedSubMessage(message.apply_transpose(enc_dict)).decrypt_message())