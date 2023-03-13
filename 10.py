word = input()
d = dict()
prev = 0
for symbol in range(len(word)):
    if symbol == 0:
        d[word[symbol]] = len(word)
        prev = len(word)
    else:
        new_count = prev - symbol + (len(word) - symbol)
        prev = new_count
        if d.get(word[symbol]) is not None:
            d[word[symbol]] += new_count
        else:
            d[word[symbol]] = new_count
word = list(set(list(word)))
word.sort()
for x in word:
    print(str(x) + ':' + ' ' + str(d[x]))