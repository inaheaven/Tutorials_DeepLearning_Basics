from gensim.models import word2vec

filename = './appendix/wiki.model'
model = word2vec.Word2Vec.load(filename)

model = word2vec.Word2Vec.load(filename)

result = model.most_similar(positive=['Python', '파이썬'])
print(result)

result = model.most_similar(positive=['아빠', '여성'], negative=['남성'])[0]
print(result)

result = model.most_similar(positive=['왕자', '여성'], negative=['여성'])[0:5]
print(result)

result = model.most_similar(positive=['서울', '일본'], negative=['한국'])[0:5]
print(result)

result = model.most_similar(positive=['서울', '중국'], negative=['한국'])
print(result)

result = model.most_similar(positive=['오른쪽', '남자'], negative=['왼쪽'])[0]
print(result)

result = model.most_similar(positive=['서울', '맛집'])[0:5]
print(result)

result = model.most_similar(positive=['서울', '맛집'], negative=['동'])[0:5]
print(result)

result = model.most_similar(positive=['고양이'])
print(result)

result = model.most_similar(positive=['강아지'])
print(result)

result = model.most_similar(positive=['월드컵', '우승', '러시아'])[0:30]
print(result)