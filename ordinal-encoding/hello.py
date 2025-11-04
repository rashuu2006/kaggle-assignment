import pandas as pd

d = {'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000], 
     'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'], 
     'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small']}

for key in d:
    if type(d[key][0]) == str:
        unique = list(set(d[key]))
        d[key] = [unique.index(v) for v in d[key]]

for i in range(len(d['sales'])):
    print(*[d[key][i] for key in d])

print("Total rows:", len(d['sales']))