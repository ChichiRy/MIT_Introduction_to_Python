# Problem Set 4B
# Name: Ryan Chironga <Chichi_Ry>
# Collaborators:
# Time Spent: x:xx

import string
import random

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")                               # Commented out to prevent multiple printing of this line when recalling load_words function
    # inFile: file                                                          # during initialising 
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")                           # Same
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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # pass #delete this line and replace with your code here
        shift_dict = {}                                                           # Initialises shifted alphabet dictionary
        letters = list(string.ascii_letters)                                      # Creates a list of uppercase and lowercase letters from string library
        index = 0                                                                 # Initialises index
        for letter in letters:                                                    # Iterates through letters in the list. For each letter, a shift is app
            if letter in string.ascii_uppercase:                                  # lied. If index overflws in either +ve or -ve directions, 26 is either
                if (index + shift) < 26:                                          # added or subtracted.
                    shift_dict[letter] = letters[(index + 26) + shift]            # Letter is then added as the value of the key in the dictionary, shift_dict.
                elif (index + shift) > 51:
                    shift_dict[letter] = letters[(index - 26) + shift]
                else:
                    shift_dict[letter] = letters[index + shift]
            elif letter in string.ascii_lowercase:
                if (index + shift) < 0:
                    shift_dict[letter] = letters[(index + 26) + shift]
                elif (index + shift) > 25:
                    shift_dict[letter] = letters[(index - 26) + shift]
                else:
                    shift_dict[letter] = letters[index + shift]
            index += 1
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # pass #delete this line and replace with your code here
        message_text = self.get_message_text()
        message_text = list(message_text)
        shift_dict = self.build_shift_dict(shift)
        encrypted_message = []                                                           # For each character in message_text, its equivalent in shift_dict
        for character in message_text:                                                   # is added. If the character is not a letter, it is directly added
            if character in string.ascii_letters:                                        # to encrypted_message as a list.
                encrypted_message.append(shift_dict[character])
            else:
                encrypted_message.append(character)
        encrypted_message = ''.join(encrypted_message)                                   # Rejoins individual list characters to form message.
        return encrypted_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # pass #delete this line and replace with your code here
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        # pass #delete this line and replace with your code here
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        # pass #delete this line and replace with your code here
        return (self.encryption_dict.copy())

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        # pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # pass #delete this line and replace with your code here
        self.shift = shift
        text = self.message_text
        PlaintextMessage.__init__(self, text, shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here
        best_shift = {}
        for shift in range (25):
            PlaintextMessage.change_shift(self, (-shift))
            decrypted_message = PlaintextMessage.get_message_text_encrypted(self)
            decrypted_message_list = decrypted_message.split(' ')
            valid_words_count = 0
            for word in decrypted_message_list:
                if is_word(self.valid_words, word):
                    valid_words_count += 1
                else:
                    continue
            best_shift_values = [0]
            for value in best_shift.values():
                best_shift_values.append(value)
            if max(best_shift_values) > valid_words_count:
                continue
            elif max(best_shift_values) == valid_words_count:
                best_shift[shift] = valid_words_count
            else:
                best_shift = {}
                best_shift[shift] = valid_words_count
        
        if len(best_shift) <= 1:
            keys = []
            for value in best_shift.keys():
                keys.append(value)
            keys = sorted(keys)
            best_shift = 26 - keys[0]
            PlaintextMessage.change_shift(self, best_shift)
            decrypted_message = PlaintextMessage.get_message_text_encrypted(self)
            return decrypted_message
        else:
            best_shift_keys = []
            for key in best_shift.keys():
                best_shift_keys.append(key)
            best_shift = 26 - random.choice(best_shift_keys)
            PlaintextMessage.change_shift(self, best_shift)
            decrypted_message = PlaintextMessage.get_message_text_encrypted(self)
            return decrypted_message

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print()
    # print('-------------------')
    # print()
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
    # print()
    # print('-------------------')
    # print()
#
    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    story = get_story_string()    
    ciphertext_2 = CiphertextMessage(story)
    print('Actual output:', ciphertext_2.decrypt_message())
    # TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
    
    # plaintext = PlaintextMessage('I am 20 years old.', 20)
    # print()
    # print('-------------------')
    # print()
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
