def is_palindrome(i, start, length):
    word =str(i)[start: start+length]
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    print word
    return True


def cartalk2(mileage):

    while mileage < 200000:
        if(is_palindrome(mileage, 2, 4) and
           is_palindrome(mileage + 1, 1, 5) and
           is_palindrome(mileage +2, 1, 4) and
           is_palindrome(mileage + 3, 0, 6)):
                        return True
        mileage = mileage + 1


print cartalk2(198888)
