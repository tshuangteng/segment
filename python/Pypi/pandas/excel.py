"""
import pandas as pd

file_path = './test.xlsx'

# # 读取一列
# df = pd.read_excel(file_path, usecols=[0], skiprows=1)
# df = pd.read_excel(file_path, usecols=[0], header=1)
df = pd.read_excel(file_path, usecols=[0])

# # 写入一列
df = pd.read_excel(file_path)
# df['last_column'] = [x for x in range(len(row_number_without_header)]
value = [x for x in range(len(row_number_without_header)]
df.insert(0, 'column_1_without_index', value=value)
df.to_csv(f'new.csv', index=False)

############################
# df = pd.read_excel(file_path)
# value = [x for x in range(80029)]
# df.insert(0, '城市名称', value=value)
# df.insert(1, '省编码', value=value)
# df.insert(2, '城市编码', value=value)
# print(df)
# df.to_csv('new.csv', index=False)
"""
