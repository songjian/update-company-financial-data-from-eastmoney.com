import pandas as pd
from eastmoney import f10
import json
import os

# 读取CSV文件
df = pd.read_csv('tdx_stocks.csv', dtype={'股票代码': str})

# 创建保存数据的目录
if not os.path.exists('zcfzb'):
    os.makedirs('zcfzb')

# 循环遍历每行数据
for index, row in df.iterrows():
    # 拼接得到股票代码
    stock_code = row['交易所简码'] + row['股票代码']

    # 请求资产负债表数据
    data = f10.zcfzb(code=stock_code)

    # 将data字段转换为DataFrame并保存为CSV文件
    try:
        pd.DataFrame(data['data']).to_csv(f'zcfzb/{stock_code}.csv', index=False)
    except KeyError:
        print(f"股票代码{stock_code}的资产负债表数据不存在")
