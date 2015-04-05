def has_no_e():
    fin = open('words.txt')
    for line in fin:
        flag = False
        word = line.strip()
        for letter in word:
            if (letter  == 'e'):
                flag = True
                break
        if flag == False:
            print word

has_no_e()
