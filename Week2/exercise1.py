import json
import re

from konlpy.tag import Twitter
from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser



def graph( wordInfo):
    font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf'  # \는 \\를 사용한다.
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)


    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    print(Sorted_Dict_Values)
    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align = 'center')

    Sorted_Dict_Keys = sorted(wordInfo, key = wordInfo.get, reverse=True)
    print(Sorted_Dict_Keys)
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation = '70')

    plt.show()


def savewordCloud( wordInfo, filename):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    print( type(taglist))

    pytagcloud.create_tag_image(taglist, filename, size = (640,480), fontname='Malgun Gothic', rectangular=False)
    webbrowser.open(filename)

def main():
    openFileName = 'jtbcnews_facebook_2016-10-01_2017-03-12.json'
    cloudImagePath = openFileName + '.jpg'

    rfile = open(openFileName, mode='r', encoding='utf-8-sig')
    rfile = rfile.read() #in bytes

    jsonData = json.loads( rfile)
    # print(jsonData)


    message = ''
    for item in jsonData:
        if 'message' in item.keys():
            message = message + re.sub(r'[^\w]', '', item['message']) + ''


    print(message)

    nlp = Twitter()
    nouns = nlp.nouns(message)

    count = Counter(nouns)
    print('count:', count)

    wordInfo = dict()
    for key, value in count.most_common(20):
        if(len(str(key))>1):
            wordInfo[key] = value
            print(key, '/', value)

    graph(wordInfo)
    savewordCloud(wordInfo, cloudImagePath)
if __name__ == '__main__':
    main()
