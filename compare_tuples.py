import random
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    print t
    t.sort(reverse=True)
    print t
    res = []
    for _, _, word in t:
        res.append(word)
    print res
    return res

t = ['prime', 'largest', 'weak', 'sea']
print sort_by_length(t)
