from konlpy.tag import Twitter
import math, sys

class BayesianFilter():

    def __init__(self):
        self.category_dict = {}
        self.word_dict = {}
        self.words = set()
        print('생성자 호출됨')

    def fit(self, text, category):
        word_list = self.bayes_split(text)
        print(word_list)
        for word in word_list:
            self.inc_word(word, category)

        self.inc_category(category)
        print('\nfit 함수 실행 결과')
        print('[category_dict 사전 내용]')
        print(self.category_dict)
        print('[word 집합 내용]')
        print(self.words)
        print('[word_dict 사전 values]')
        print(self.word_dict)

    def bayes_split(self, text):
        results = []
        twitter = Twitter()

        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])

        return results

    def inc_word(self, word, category):
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0;
        self.word_dict[category][word] += 1;
        self.words.add(word)

    def inc_category(self, category):
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        print('모든 카테고리들의 빈도수 총합')
        print(sum_categories)
        print('해당 카테고리의 빈도수')
        print(category_v)
        return category_v/ sum_categories

    def word_prob(self, word, category):
        # print(word, category)
        n = self.get_word_count(word, category) + 1
        d = sum(self.word_dict[category].values()) + len(self.words)

        print("n: ", n)
        print("d: ", d)
        return n/d

    def get_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0

    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize
        words = self.bayes_split(text)
        score_list = []

        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category, score))

            print('스코어')
            print(score)
            print(max_score)
            if score > max_score:
                max_score = score
                best_category = category

        print("베스트 카테고리")
        print(best_category)
        return best_category, score_list

bf = BayesianFilter()

print("*"*100)
bf.fit('세일 무료 배송 할인', "광고")
print("*"*100)
bf.fit("일정 확인", "중요")
print("*"*100)
bf.fit("백화점 세일", "광고")
print("*"*100)
bf.fit("파격 세일 할인", "광고")
print("*"*100)
bf.fit("쿠폰 선물 & 무료 배송", "광고")
print("*"*100)
bf.fit("프로젝트 진행 상황", "중요")
print("*"*100)
bf.fit("봄과 함께 찾아온 따뜻한 신제품 소식", "광고")
print("*"*100)
bf.fit("인기 제품 기간 한정 세일", "광고")
print("*"*100)
bf.fit("계약 잘 부탁드립니다", "중요")
print("*"*100)
bf.fit("회의 일정이 등록되었습니다", "중요")
print("*"*100)
bf.fit("오늘 일정이 없습니다", "중요")
print("*"*100)

print("=="*100)


pre, scorelist = bf.predict('무료 배송')
print("결과", pre)
print(scorelist)

