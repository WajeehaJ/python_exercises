

def sed(pattern_str, replace_str):
    try:    
        fin = open('words2.txt')
        fout = open('copy_words.txt', 'w')
        for line in fin:
            t = line.split()
            for x in t:
                mystr = x.replace(pattern_str, replace_str)
                fout.write(mystr)
                fout.write('\n') 
        fin.close()
        fout.close()
    except:
        print 'Something went wrong.'


sed('salted', 'tasted')
