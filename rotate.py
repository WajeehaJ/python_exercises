import string



def rotate_letter(letter, n):
    """
    function that rotates a letter
    by the value n
    """
    if letter.isupper():
        start = ord('A')
    else:
        start = ord('a')

    c = ord(letter) - start
    r = (c+n) % 26 + start

    return chr(r)

def rotate_word(word, n):
    """
    function that rotates a string
    by the value n
    """
    res = ''
    for i in word:
        res += rotate_letter(i, n)
    return res

word = 'cheer'

print rotate_word('cheer', 7)
print rotate_word('steer', 7)
