# i = float(input("输入圆的半径："))
# print("圆的周长："+str(2*3.14*i))
# print("圆的面积："+str(3.14*(i**2)))
# 一个字符串只能有一种数据格式
# 如何把数字变成字符串：str()
"""
if的写法
if i = 1:  # 第一种条件
    print("i=1')  # 满足后运行这条
elif i = 2:  # 第二种条件
    print("i=2")
else:  # 如果都不满足的化。如果只有两个条件，那么可以只用else。如果else不执行任何操作可以不要else
    print("else")
"""
i = float(input("输入年份："))
n = i % 4
if n == 0:
      print("这是闰年")
else:
    print("这不是闰年")
