# base case = if input is 1 or nothing then answer is that thing or empty list
# if sequence is longer than 1 character, identify simpler version of problem

# if we were given all permutations of everything but first character,
# we can get all permutations with character if we just loop over inserting it at different places
# its -> it -> it,ti -> sit, ist, its,  
def permutations(s, dup = True):
    """"Given any string input, return a list of all different permutations.
    If dup = True (default), return duplicate permutations"""
    assert isinstance(s,str), 'Given input is not a string'
    if len(s) <= 1: # base case
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]): # wil return a list of all lower order perms once it comes back up
            for i in range(len(e)+1): # for o to len(e), compute all the perms by inserting the element that was taken away
                perms.append(e[:i] + s[-1] + e[i:])
        if dup == True: # return the final list with or without duplicates.
            return perms
        else:
            res = []
            [res.append(el) for el in perms if el not in res]
            return res

if __name__ == '__main__':
    pass # test cases here

print(permutations('1a11'))

# Caesar Cipher: Pick integer and shift every letter by that integer to other letters in the alphabet. Be carefull with extremes
# let's map uppercase to upercase, lowercase to lowercase, and keep punctuation and spaces
# use message class with 2 subclasses: ciphertext, plaintext
# give message class methods that can be used to encrypt or decrypt message
# paintext class has methods to encode a string with a specific shift value
# ciphertext contains a method used to decode the string
