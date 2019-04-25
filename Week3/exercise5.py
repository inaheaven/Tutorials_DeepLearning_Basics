import pymysql
import matplotlib.pyplot as plt
import matplotlib
from pandas.core.series import Series
from pandas.core.frame import DataFrame
from matplotlib import font_manager, rc
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='vkdlskf',
                       db='python_tutorial', charset='utf8')

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL문 실행
sql = "select * from three_country"
cur.execute(sql)

# 데이타 Fetch
# rows = cur.fetchall()
# print(rows)  # 전체 rows

data0 = []
data1 = []
data2 = []

for result in cur:
    print(result)
    data0.append(result[0])
    data1.append(result[1])
    data2.append(result[2])

myseries = Series(data2, index=[ data0, data1])
print(myseries)

df = myseries.unstack()
print(df)

font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf' # \는 \\를 사용한다.
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

df.plot(kind='barh', rot=0)
plt.title('3개국 테러 발생 현황')

plt.show()

cur.close()
# Connection 닫기
conn.close()