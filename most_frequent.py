import random 

def most_frequent(s):
    """ Sort the letter in s in reverse order of
        frequency
    s: string
    Returns: list of letters    
    """

    hist = make_histogram(s)
    t = []
    for x,freq in hist.iteritems():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)

    return res

def make_histogram(s):
    """ Make a map from letter to number of times
        they appear in s
    s: string 
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist [x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
    """ Return the contents of a file as a sring """
    return open(filename).read()

if __name__ == '__main__':
    s = read_file('words.txt')
    t = most_frequent(s)
    for x in t:
        print x  
    	
    

