# -*- coding: utf-8 -*-
# @Author  : shuya
# @Time    : 2023/9/18 15:44
# @File    : device_comsumption.py
# @Description:

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
import subprocess
import matplotlib

matplotlib.rc("font", family='Songti SC')


def percent_data(df):
    kitchen = df['厨房的有功功率'].sum()
    laundry = df['洗衣房的有功功率'].sum()
    air_conditioner = df['电热水器和空调的有功功率'].sum()
    print(kitchen, laundry, air_conditioner)
    plt.figure(figsize=(6, 6))
    size = pd.Series([kitchen, laundry, air_conditioner])  # 数据
    label = ['厨房的有功功率', '洗衣房的有功功率', '电热水器和空调的有功功率']
    plt.pie(size, labels=label, autopct='%.2f%%', colors=['peachpuff', 'pink', 'lightskyblue'])
    plt.title('不同类别电器的有功功率')
    plt.show()


if __name__ == '__main__':
    # mpl_fonts = set(f.name for f in FontManager().ttflist)
    #
    # print('all font list get from matplotlib.font_manager:')
    # for f in sorted(mpl_fonts):
    #     print('\t' + f)
    size = pd.Series([1, 3, 4])  # 数据
    plt.pie(size,  autopct='%.1f%%', colors=['peachpuff', 'pink', 'lightskyblue'])
    plt.show()

