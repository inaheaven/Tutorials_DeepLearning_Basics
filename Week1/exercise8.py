import webbrowser
import pytagcloud
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fp = codecs.open("BEXX0003.txt", "r", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body > text")
text = body.getText()


# print(text)


twitter = Twitter()
word_dic = {}

lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun":
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1

print(word_dic)

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse= True)
print(keys)


def saveWorldCloud( wordInfo):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize = 80)
    print(type(taglist))
    filename = 'wordcloud.png'

    pytagcloud.create_tag_image(taglist, filename, size=(640,480), fontname='Malgun Gothic', rectangular=False)
    webbrowser.open(filename)

def showGraph ( wordInfo):
    font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf'  # \는 \\를 사용한다.
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요단어')
    plt.ylabel('빈도 수')
    plt.grid(True)

    sorted_dict_values = sorted(wordInfo.values(), reverse=True)
    print(sorted_dict_values)
    plt.bar(range(len(wordInfo)), list(sorted_dict_values), align='center')

    sorted_dict_values = sorted(wordInfo, key=wordInfo.get, reverse=True)
    print(sorted_dict_values)
    plt.xticks(range(len(wordInfo)), list(sorted_dict_values), rotation='70')

    plt.show()

wordInfo = dict()
for word, count in keys[:500]:
    # print("{0}({1})".format(word, count), end=" ")
    if(count >60 and len(word) >= 2):
        wordInfo[word] = count

saveWorldCloud(wordInfo)
showGraph(wordInfo)
print(wordInfo)