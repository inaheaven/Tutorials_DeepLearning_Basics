# font_manager : 폰트 사용/찾기/매니저 역할을 하는 객체
# rc 함수 : matplotlib의 글자/색상 등의 설정을 가능하게 해주는 함수
from matplotlib import font_manager, rc
import matplotlib
import matplotlib.pyplot as plt

font_location = '/Volumes/MicroSD/Workspace/Neural Networks and Deep Learning/malgun.ttf' # \는 \\를 사용한다.
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

plt.plot([1,2,3,4], [5,6,7,8])
plt.xlabel('x축 한글 표시')
plt.title('matplotlib 활용')
plt.show()