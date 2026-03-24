#2

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

train=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_2_train.csv')
test=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_2_test.csv')

print(train.info())
print(test.info())

train_x=train.drop(['gas_total'], axis=1)
train_y=train['gas_total']
test_x=test.drop(['gas_total'], axis=1)
test_y=test['gas_total']

train_x,train_y=train_test_split(train_x,train_y,test_size=0.2,random_state=42)

cate_cols=train_x.select_dtypes(include=['object']).columns
num_cols=train_x.select_dtypes(include=['number']).columns

encoder=OneHotEncoder(sparse=False, handle_unknown='ignore')
train_x[cate_cols]=encoder.fit_transform(train_x[cate_cols])
test_x[cate_cols]=encoder.transform(test_x[cate_cols])



