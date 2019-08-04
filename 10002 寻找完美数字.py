"""
取得所有的完美数
这是python-100 day的一个练习
完美数是指，一个数等于除自己外的所有因子之和
因子是所有可以被整除的数
Author: 蓝为一
Date: 2019年8月3日07:02
"""
# 寻找完全数，即完美数字（Perfect Number)
factor_list = []  # 定义一个用来装因子的列表
for n in range(1, 10000):  # n厉遍1-10000的数字，因为超过一万的下个完美数字是33550336，数字太大了
    for i in range(1, n):  # i是分子，用来确认是否是可以被整除的因子，以后你此时1到n-1的数字
        if n % i == 0:  # 如果n能被i整除
            factor_list.append(i)  # 那么就把这个i放在列表里里面去
    if n == sum(factor_list):  # 如果厉遍了i之后，列表中所有因子之和等于n，那么就把这个n打印出来。之前又想过也把n放在一个列表里面，也是没问题的
        print(n)
    else:
        list.clear(factor_list)  # 如果不等于n，那么装因子的列表就要清空。因为不要影响下个循环
