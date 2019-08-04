"""
这是我尝试用所学的代码制作一个快速计算的工具
将华摄氏度和摄氏度进行转换
目前有几个问题没解决
1. 结算完之后如何回到最开始重新输入？
2. 如何判断如果结果是整数就显示整数，如果是小数就显示2位小数？我当然知道用if可以解决...

蓝为一
2019年8月2日 11:17
"""

print("你想进行那种转换？\n1.华摄氏度 to 摄氏度\n2.摄氏度 to 华摄氏度")
choice = input("请输入序号：")  # 201908020026 最开始不知道怎么样将input的数字作为变量了
if choice == '1':
    Fahrenheit = input("请输入华摄氏度：")
    if float(Fahrenheit) < -459.67:
        print("该温度低于绝对零度，程序结束")
    elif float(Fahrenheit) > 100000:
        print("你输入的数值过大，程序结束")
    else:
        Celsius_Result = (float(Fahrenheit) - 32) / 1.8
        print(str(round(Celsius_Result,2))+"摄氏度")  # 还是没弄清楚，为什么这里的round里面的都好会有一个报错提示
elif choice == '2':
    Celsius = input("请输入摄氏度：")
    if float(Celsius) < -273.15:
        print("该温度低于绝对零度，程序结束")
    elif float(Celsius) > 100000:
        print("你输入的数值过大，程序结束")
    else:
        Fahrenheit_Result = float(Celsius)*1.8+32
        print(str(round(Fahrenheit_Result,2))+"华摄氏度")
else:
    print("输入错误，程序结束")
