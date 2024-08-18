import pandas as pd

df = pd.read_csv(r"A:\kaggle\netflix1.csv")

# print(df.head())
# print(df.tail())
# print(df.columns)

df.drop(columns='rating', inplace= True)
# print(df.columns)

new_col = []
for i in df.columns:
    new_col.append(i.capitalize())

df.columns = new_col
# print(df.columns)

# print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

# print(df.isnull().sum())

df.dropna(inplace=True)
# print(df['Show_id'].nunique())

s = []
for i in df['Show_id']:
    s.append(i.replace('s',''))

df['Show_id'] = s
# print(df['Show_id'])

# print(df['Date_added'])

n=[]
for d in df['Date_added']:
    n.append(d.replace('/','-'))

df['Date_added']=n
# print(df['Date_added'])    

# print(df.head())
# print(df.tail())
# print(df.columns)


df.dropna(how='any',inplace=True)
print(df)


df.to_csv(r"A:\kaggle\Netflix.csv", index= False)




