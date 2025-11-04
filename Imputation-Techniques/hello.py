import pandas as pd

def impute_missing(df):
    df = df.replace('nan', 'missing')
    for col in df.columns:
        clean = [v for v in df[col] if v != 'missing']
        if not clean or 'missing' not in df[col].values:
            continue
        if all(isinstance(v, (int, float)) for v in clean):
            clean.sort()
            val = clean[len(clean)//2]
        else:
            val = max(set(clean), key=clean.count)
        df[col] = df[col].replace('missing', val)
    return df
data = {'index':[0,1,2,3,4,5,6,7,8,9,10,11],
        'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000],
        'city': ['Tampa','Tampa','Orlando','Jacksonville','nan','Jacksonville','Miami','Miami','Orlando','Orlando','nan','Orlando'],
        'rating':[5,4,'nan',3,5,4,'nan',3,5,4,5,2]}

df = impute_missing(pd.DataFrame(data))
print(df)