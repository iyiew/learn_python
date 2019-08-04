"""
斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ........
这个数列从第3项开始，每一项都等于前两项之和。
Author: 蓝为一
Date: 2019年8月3日12:21
"""
the_list = [1, 1]  # 先把前2项列出来
for n in range(1, 1000000):  # 给个区间不然无限计算下去了
    if n == int(the_list[len(the_list)-1]) + int(the_list[len(the_list)-2]):  # 如果遍历到的数字，等于表中最后两位之和
        the_list.append(n)  # 那么就把这个数字也计入列表中
print(the_list)  # 最后输出这个列表
