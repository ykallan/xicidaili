import pandas as pd

data = pd.read_csv('proxy2.csv', encoding='utf-8')
print(data['IP地址'][2])
print(data.columns)

# print(data['类型'])

print(len(data))

for i in range(len(data)):
    print(data['类型'][i]+"://"+data['IP地址'][i]+":"+data['端口'][i])
    # break