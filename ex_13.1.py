import string

def read_file(filename):
    """ Return the contents of a file as a sring """
    return open(filename).read()


if __name__ == '__main__':
    s = read_file('book_section.txt')
    t = s.split(' ')
    for word in t:
        word = word.replace(' ', '')
        word = word.translate(string.maketrans("",""), string.punctuation + string.whitespace)
        if word != '':
            print word.lower(),

