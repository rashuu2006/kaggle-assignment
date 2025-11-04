import pandas as pd

def one_hot_encode(df, cols):
    result = df.copy()
    for col in cols:
        result[col] = result[col].fillna('missing').astype(str).str.lower()
        for val in result[col].unique():
            result[f"{col}_{val}"] = (result[col] == val).astype(int)
        
        result = result.drop(col, axis=1)
    return result
d = {
    'sales': [100000, 222000, 1000000, 522000, 111111, 222222, 1111111, 
              20000, 75000, 90000, 1000000, 10000],
    'city': ['Tampa', 'Tampa', 'Orlando', 'Jacksonville', 'Miami', 
             'Jacksonville', 'Miami', 'Miami', 'Orlando', 'Orlando', 
             'Orlando', 'Orlando'],
    'size': ['Small', 'Medium', 'Large', 'Large', 'Small', 'Medium', 
             'Large', 'Small', 'Medium', 'Medium', 'Medium', 'Small']
}
df = pd.DataFrame(d)
encoded_df = one_hot_encode(df, ['city', 'size'])
print(encoded_df)