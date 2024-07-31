import os
import json

# 定义一个空列表存储所有数据
all_data = []

# 指定文件夹路径
folder_path = "C:\\Users\\22597\\OneDrive\\桌面\\数据文件 2024.4.4"

# 获取文件夹下所有文件
file_list = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# 读取每个JSON文件并将数据存入列表
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as f:
        data = json.load(f)
        all_data.append(data)

import csv

# 定义CSV文件路径
csv_file_path = "output.csv"

# 定义列名，它们应与字典中的键相同
column_names = ['br', 'sr', 'imbalance_force', 'wob', 'torque', 'rop', 'rpm', 'fn', 'workrate_fn']

# 打开CSV文件并创建一个写入器对象
with open(csv_file_path, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 写入列名
    writer.writerow(column_names)

    # 遍历all_data中的每个字典，并将字典的值写入CSV文件的一行
    for item in all_data:
        row_values = [
            item['br'],
            item['sr'],
            item['imbalance_force'],
            item['wob'],
            item['torque'],
            item['rop'],
            item['rpm'],
            json.dumps(item['fn']),  # 将fn列表嵌套结构转换为JSON字符串以便在CSV中表示
            json.dumps(item['workrate_fn'])  # 同理处理workrate_fn
        ]
        writer.writerow(row_values)

print("Data successfully written to", csv_file_path)