import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='genism')

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp = codecs.open(filename='BEXX0003.txt', mode='r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text')
text = body.getText()
# print(text)

twitter = Twitter()
results = []

lines = text.split('\r\n')
# print(lines)


for line in lines:
    malist = twitter.pos(line, norm= True, stem= True)
    print(malist)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])

    r1 = (" ".join(r)).strip()
    results.append(r1)

    print(r1)

print(results)
wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))    

data = word2vec.LineSentence(wakati_file)
print(type(data))
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
print(type(model))

saved_file_name = 'toji.model'
model.save(saved_file_name)
print('파일', saved_file_name, '저장 완료')