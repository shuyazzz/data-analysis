# -*- coding: utf-8 -*-
# @Author  : shuya
# @Time    : 2023/9/18 15:33
# @File    : main.py
# @Description:

import pandas as pd
import numpy as np
from preprocess import dirty_data, preprocess
from device_comsumption import percent_data


def load_data():
    data = pd.read_csv('../data/household_power_consumption.csv', index_col=0)
    print(data[:2])
    print(data.columns)
    data.rename(columns={
        'Date': '日期',
        'Time': '时间',
        'Global_active_power': '有功功率',
        'Global_reactive_power': '无功功率',
        'Voltage': '电压',
        'Global_intensity': '电流',
        'Sub_metering_1': '厨房的有功功率',
        'Sub_metering_2': '洗衣房的有功功率',
        'Sub_metering_3': '电热水器和空调的有功功率',
    }, inplace=1)
    print(data.columns)
    print(data[:2])
    return data


if __name__ == '__main__':
    data = dirty_data(load_data())
    data = preprocess(data)
    print(data[:2])
    percent_data(data)

