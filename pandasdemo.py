import pandas as pd

df = pd.read_excel('shuju.xlsx')
df['s_date'] = pd.to_datetime(df['s_date'])
df = df.set_index('s_date')
#每月某用户总评论量
x = []
y = []
data = df[df['s_nameId'] == '择城终老'].resample('M')['s_comment'].max().reset_index(drop=False)
for index, row in data.iterrows():
    if pd.isnull(row['s_comment']):
        y.append(0)
    else:
        y.append(row['s_count'])
    x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
print(x)
print(y)
'''
#每月各个用户输出帖子数
name_df = df.groupby('s_nameId', as_index=False)
x = []
y = []
for name, group in name_df:
    data = group.resample('M').count().reset_index(drop=False)  # 每个总帖子数
    data2 = data[data['s_date'] == '2018-01-31']
    if len(data2.values.tolist()) <= 0 or data2.values.tolist()[0][3] <= 0:
        continue
    else:
        x.append(data2.values.tolist()[0][3])
        y.append(name)
print(x)
print(y)
'''
'''
#每月某个用户输出帖子数
x = []
y = []
data = df[df['s_nameId'] == '择城终老'].resample('M').count().reset_index(drop=False)
for index, row in data.iterrows():
    y.append(row['s_url'])
    x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
print(x)
print(y)
'''
'''
#每月某用户总浏览量
x = []
y = []
data = df[df['s_nameId'] == '择城终老'].resample('M').sum().reset_index(drop=False)
for index, row in data.iterrows():
    y.append(row['s_count'])
    x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
print(x)
print(y)
'''
'''
#每月某用户总评论量
x = []
y = []
data = df[df['s_nameId'] == '择城终老'].resample('M').sum().reset_index(drop=False)
for index, row in data.iterrows():
    y.append(row['s_comment'])
    x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
print(x)
print(y)
'''
'''
#每月某用户总浏览量
x = []
y = []
data = df[df['s_nameId'] == '择城终老'].resample('M')['s_count'].max().reset_index(drop=False)
for index, row in data.iterrows():
    if pd.isnull(row['s_count']):
        y.append(0)
    else:
        y.append(row['s_count'])
    x.append(str(row['s_date'].year)[-2:] + str(row['s_date'].month))
print(x)
print(y)
'''
