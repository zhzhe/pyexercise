import pandas as pd

#Define excel flies path
CaiWuShare = 'D:/财务共享.xlsx'

df = pd.DataFrame({'ID':(1,2,3),'name':('zz','xx','yy')})

df.to_excel(CaiWuShare)


