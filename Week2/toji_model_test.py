from gensim.models import word2vec
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from pandas.core.frame import DataFrame

def showGraph( somedata ):
    font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf'  # \는 \\를 사용한다.
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name) 
    
    su = len(somedata) # 전체 데이터 수
    
    # 축에 보여질 항목 이름들
    item = list( item[0] for item in somedata)
    
    # 그려지는 수치 데이터 
    count = list( item[1] for item in somedata)

    plt.barh(range(su), count, align='center')
    plt.yticks(range(su), item, rotation='10')
    plt.xlim(0.8, 0.86)
    plt.grid(True)  
    plt.show()    

filename = 'toji.model'

model = word2vec.Word2Vec.load( filename )

somedata = model.most_similar(positive=['땅'])

showGraph( somedata )

print(somedata)
# [('조상', 0.842327356338501), ('작정', 0.8393210768699646), 
# ('사시', 0.8242330551147461), ('까지', 0.8217380046844482), 
# ('대가', 0.8211498260498047), ('낚아채', 0.8196094632148743), 
# ('남루', 0.8175667524337769), ('그러믄', 0.8160238265991211), 
# ('전답', 0.8147901296615601), ('넘기다', 0.8142741918563843)]

print( model.most_similar(positive=['집']))

# [('남정', 0.7779189944267273), ('구석', 0.7696069478988647), 
# ('아비', 0.7626349925994873), ('나선', 0.7500041723251343), 
# ('돌아가다', 0.7449293732643127), ('늦다', 0.7445415258407593), 
# ('째', 0.7424589395523071), ('사오다', 0.7324668169021606), 
# ('우우', 0.7303623557090759), ('계란', 0.7302969694137573)]