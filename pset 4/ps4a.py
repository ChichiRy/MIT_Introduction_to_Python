# Problem Set 4A
# Name: Ryan Chironga <Chichi_Ry>
# Collaborators:
# Time Spent: approx. 4h30

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # pass #delete this line and replace with your code here
    
    permutation_sequence = list(sequence)   #Provides iterable list from string
    permutations_dictionary = {}            #Dictionary and list initialisation
    permutations_list = []
    first_char = permutation_sequence[0]    #Fetches the first character of the string, saves it to first_char
    permutation_sequence.remove(first_char) #, and removes it
    
    if len(permutation_sequence) == 1:                                          #recursive base case
        permutation_sequence = ''.join(permutation_sequence)                    #returns a string rather than a letter
        for index in range (2):                                                 #index to determine position of added letter; loop ensures all permutations are tried
            new_permutation = list(permutation_sequence)                        #returns an iterable list
            new_permutation.insert(index, first_char)                           #inserts removed character at specified index
            new_permutation = ''.join(new_permutation)                          #returns a string rather than a list
            permutations_list.append(new_permutation)                           #adds new permutation to the list
        return permutations_list                                                #returns list to caller
    
    else:                                                                       #recursive case
        permutations_list = get_permutations(''.join(permutation_sequence))     #recursive call (No -ve since function already removes first character, otherwise it'd be double deduction)
        permutation_list = permutations_list.copy()                             #copies list to allow iteration
        for permutation in permutation_list:                                    #iterates over each available incomplete permutation in the list
            for index in range (len(permutation) + 1):                          #index to determine position of added letter; loop ensures all permutations are tried
                new_permutation = list(permutation)                             #returns an iterable list
                new_permutation.insert(index, first_char)                       #inserts removed character at specified index
                new_permutation = ''.join(new_permutation)                      #returns a string rather than a list
                if new_permutation not in permutations_dictionary:              #avoids duplication of items in list, saves memory
                    permutations_list.append(new_permutation)
                    permutations_dictionary[new_permutation] = permutations_dictionary.get(new_permutation, 0) + 1         
                else:
                    continue
        permutation_list.clear()                                                #Gets rid of 'garbage' from running the function
        for permutation in permutations_dictionary.keys():                      #adds all dictionary keys to list to be returned
            permutation_list.append(permutation)
        permutation_list.sort()                                                 #orders list before returning
        return permutation_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here
    
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    
    # example_input = 'abcd'
    # print('Input:', example_input)
    # print('Expected Output:', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bdca', 'bdac', 'bcda', 'bcad', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
    # print('Actual Output:', get_permutations(example_input))
    
    # example_input = 'none'
    # print('Input:', example_input)
    # print('Expected Output:', ['none', 'enon', 'nnoe', 'noen', 'onen', 'neno', 'onne', 'enno', 'neon', 'eonn', 'oenn', 'nneo'])
    # print('Actual Output:', get_permutations(example_input))
    
    sequence = str(input('Please enter a string to permutate: ')).strip().lower()   #Asks and lowers case of string
    print('---------')
    print('Possible permutations are: ', get_permutations(sequence))            #Calls get_permutation function and displays results