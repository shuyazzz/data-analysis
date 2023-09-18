# -*- coding: utf-8 -*-
# @Author  : shuya
# @Time    : 2023/9/18 15:51
# @File    : preprocess.py
# @Description:

import numpy as np
import pandas as pd


def outliers(data):
    """
    :param data: DataFrame
    :return:  DataFrame
    desc: 异常值处理
    """
    print(data.dtypes)  # 查看字段类型，其中一些object类型数据应转换为数值型数据
    #  将异常值替换为空值
    data = data.replace('?', np.NAN)
    # 将有功功率、无功功率、电压、电流、厨房的有功功率、洗衣房的有功功率object类型数据都转换为数值型数据
    for i in list(data.columns)[2:-1]:
        data[i] = data[i].astype(float)  # 转化时候报错ValueError: could not convert string to float: '?'
    print(data.dtypes)  # 查看字段类型,看是否转化成功
    # 统一日期列数据形式
    data['日期'] = data['日期'].str.replace('/07', '/2007')
    return data


def dup_data(data):
    """
    :param data: DataFrame
    :return: DataFrame
    desc: 异常值处理
    """
    print(data.duplicated().sum())  # 查看数据是否有重复值
    return data


def null_data(data):
    """
    :param data: DataFrame
    :return: DataFrame
    desc: 缺失值处理
    """
    # 直接删除空值的行
    # data.dropna(how='any')
    # 均值填充
    # data['有功功率'].fillna(data['有功功率'].mean())
    # 线性插值
    data = data.interpolate()
    return data


def dirty_data(data):
    """
    :param data: DataFrame
    :return: DataFrame
    """
    data = outliers(data)
    data = dup_data(data)
    return data


def preprocess(df):
    # 将日期、时间转换为str类型
    df['日期'] = df['日期'].astype(str)
    df['时间'] = df['时间'].astype(str)
    # 重构index数据为包含年月日时分秒的完整时间
    df.index = pd.to_datetime(df['日期'] + ' ' + df['时间'], format='%d/%m/%Y %H:%M:%S')
    df = df.drop(['日期', '时间'], axis=1)
    return df
