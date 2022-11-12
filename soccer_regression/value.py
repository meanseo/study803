import pandas as pd

train = pd.read_csv("./data/FIFA_train.csv")
test = pd.read_csv("./data/FIFA_test.csv")

print(train.head(5))