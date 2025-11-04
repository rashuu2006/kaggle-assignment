import pandas as pd

d = {'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000], 
     'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'], 
     'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small']}
df=pd.DataFrame(d)
def encode_dataframe(df):
     for key in df:
           if type(df[key][0]) == str:
             unique = list(set(df[key]))
             df[key] = [unique.index(v) for v in df[key]]
     return df
encoded_df = encode_dataframe(df)

for i in range(len(encoded_df)):
    print(*[encoded_df[key][i] for key in encoded_df])

print("Total rows:", len(encoded_df))