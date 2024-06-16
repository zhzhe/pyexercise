
import pandas as pd

d_dict = {'A':[1,5,9], 'B':[2,6,10], 
          'C':[3,7,11], 'D':[4,8,12]}
df = pd.DataFrame(data=d_dict)

# 逐行迭代
sum = 0
for  i, row in df.iterrows():
    sum += row['A']
print(sum)

# 元组迭代器
sum = 0
for row in df.itertuples():
    sum += row.A
print(sum)