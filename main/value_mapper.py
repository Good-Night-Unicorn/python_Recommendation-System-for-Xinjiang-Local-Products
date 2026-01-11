import os
import sys
from decimal import Decimal

# 读取环境变量中的 title 参数
x_index = int(sys.argv[1])
y_index =  sys.argv[2]
status_index = int(sys.argv[4])
for line in sys.stdin:
    try:
        # 读取输入数据, 按照逗号分隔
        lists = line.strip().split(',')

        if lists[0]=="id":
            continue
        if status_index>0 && lists[status_index] not in ['已支付', '已发货', '已完成']:
            continue
        x_value = lists[x_index]
        if y_index.__contains__(","):
            y_value=""
            for i,y in enumerate(y_index.split(",")):
                if i >= len(y_index.split(","))-1:
                    y_value = y_value + lists[int(y)]
                else:
                    y_value = y_value + lists[int(y)] + ","
            print(f"{x_value}\t{y_value}")
        else:
            print(f"{x_value}\t{lists[int(y_index)]}")
    except Exception as e:
        continue
