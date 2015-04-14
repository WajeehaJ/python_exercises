from rotate import rotate_word

def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d

def find_rotatepair(t, dic):
    """
    function to find the rotate pairs
    in the list
    t: list containing rotated pairs
    """
    for i in t:
        rotated = rotate_word(i, 7)
        if rotated in dic:
            print rotated, word


t = {'jolly', 'cheers', 'zally', 'steer', 'fear'}
d = make_word_dict()

find_rotatepair(t, d)




