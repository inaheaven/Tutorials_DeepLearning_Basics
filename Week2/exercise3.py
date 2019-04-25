from gensim.models import word2vec
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

def showGraph(somedata):
    font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf'  # \는 \\를 사용한다.
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    su = len(somedata)

    item = list( item[0] for item in somedata)
    count = list(item[1] for item in somedata)

    plt.barh(range(su), count, align='center')
    plt.yticks(range(su), item, rotation='10')
    plt.xlim(0.8, 0.86)
    plt.grid(True)
    plt.show()

filename = 'toji.model'
model = word2vec.Word2Vec.load(filename)
somedata = model.most_similar(positive=['땅'])

showGraph(somedata)
print(somedata)
print(model.most_similar(positive=['집']))

