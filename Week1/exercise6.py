word_dic = {}
malist = [('사랑','noun'), ('이','조사'), ('사랑','noun'), ('바보','noun')]

for word in malist:
    if word[1] == "noun":
        if not (word[0] in word_dic):
            word_dic[word[0]] = 0
        word_dic[word[0]] += 1

print(word_dic)