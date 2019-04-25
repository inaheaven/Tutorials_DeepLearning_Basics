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
sql = "select * from country_summary_top_10"
cur.execute(sql)

# 데이타 Fetch
# rows = cur.fetchall()
# print(rows)  # 전체 rows

data = []
myindex = []

for result in cur:
    print(result)
    data.append(result[1])
    myindex.append( result[0])

font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf' # \는 \\를 사용한다.
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

chartData = Series(data, index= myindex)
chartData.plot(kind='bar', rot=18, grid=True, title='범죄 빈도수 탑 10 국가', alpha=0.7)

plt.show()

cur.close()
# Connection 닫기
conn.close()