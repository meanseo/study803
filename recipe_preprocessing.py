import pandas as pd

data = pd.read_csv('data/recipe_data.csv', encoding="cp949")
data.rename(columns=data.iloc[0], inplace=True) # 0번째 열을 칼럼명으로 지정
data.drop(0, axis=0, inplace=True) #0번째 열 삭제
data = data[['레시피일련번호','요리명','스크랩수','요리방법별명','요리내용']] # 특정 칼럼 추출
print(data.head(5))