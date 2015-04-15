"""
Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.
"""

def read_file(filename):
    """ Return the contents of a file as a sring """
    return open(filename).read()

def print_anagram_wordlist(word_list):
    """
    Print all the anagram words in the word list
    by using the letters(tuple) of the anagram
    as a key in the dictionary
    """
    d = {}
    for word in word_list:
        if word != '':
            temp_word = ''.join(sorted(word))
            seq_letters = tuple(temp_word)
            if  seq_letters not in d:
                d[seq_letters] = [word]
            else:
                d[seq_letters] += [word]

    for _, value in d.iteritems():
        print value

if __name__ == '__main__':
    s = read_file('words.txt')
    d = {}
    word_list = s.split('\n')
    print_anagram_wordlist(word_list)

