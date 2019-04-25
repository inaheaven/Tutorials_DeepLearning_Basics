import pymysql
import matplotlib.pyplot as plt
import matplotlib
from pandas.core.series import Series
from matplotlib import font_manager, rc


# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='vkdlskf',
                       db='python_tutorial', charset='utf8')

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL문 실행
sql = "select bungi, mycount from bungitable order by ordering"
cur.execute(sql)

data = []
myindex = []

total = 0
for result in cur:
    print(result)
    total += result[1]
    data.append(result[1])
    myindex.append(result[0])

print(total)
print(data)
print(myindex)

newindex = []
for idx in range(len(myindex)):
    newindex.append(myindex[idx]
                    + '\n(' +str(round(100 * data[idx]/total, 2)) +'%)')

print(newindex)

font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf' # \는 \\를 사용한다.
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

chartData = Series(data, index = newindex)
chartData.plot(kind='pie', title='분기별 범죄 빈도')
plt.show()
cur.close()
conn.close()