import pandas as pd 
d = {'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000], 'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'], 'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small',]}
df = pd.Dataframe(data=d)
df.head(10)
df['size'].unique()
sizes=['Small','Medium','Large']
from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(categories=[sizes])
enc.fit_transform(df[['size']])
df.head()
df['size'] = enc.fit_transform(df[['size']])
df.head()
df.head(10)

