import numpy as np
import pandas as pd
tech={'Fees': [20000,25000,23000,np.NaN,26000],
'Duration':['30 Days','50 Days','30 Days','35 Dys','40 Days']}
df=pd.DataFrame(tech)
print(df)
# lambda function
df['Fees']= df['Fees'].map(lambda x:x==(x*10/100))
print(df)