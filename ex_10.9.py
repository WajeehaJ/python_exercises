def remove_duplicate(t):
    copy_t = []
    for i in t:
        if i not in copy_t:
            copy_t.append(i)
    return copy_t

letters = ['a', 'c', 'a', 'b']

result =  remove_duplicate(letters)

print result
