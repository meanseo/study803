from importlib.resources import contents
import re
import pandas as pd

data = pd.read_csv('data/recipe_data.csv', encoding="cp949")
data.rename(columns=data.iloc[0], inplace=True) # 0번째 열을 칼럼명으로 지정
data.drop(0, axis=0, inplace=True) #0번째 열 삭제
data = data[['레시피일련번호','요리명','스크랩수','요리방법별명','요리내용']] # 특정 칼럼 추출
print(data['요리내용'])
# data.info()
'''
 0   레시피일련번호  128400 non-null  object
 1   요리명      126310 non-null  object
 2   스크랩수     128400 non-null  object
 3   요리방법별명   128400 non-null  object
 4   요리내용     127340 non-null  object
'''

for i in range(1, len(data.index)):
    word = ['[재료]', '[필수재료]', '[지급재료]']
    content = data.loc[i,'요리내용']
    res = re.sub(word,'', content)
print(content)