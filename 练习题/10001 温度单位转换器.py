"""
这是我尝试用所学的代码制作一个快速计算的工具
将华摄氏度和摄氏度进行转换
Author: 蓝为一
Date: 2019年8月2日 11:17
"""

print("你想进行那种转换？\n1.华摄氏度 to 摄氏度\n2.摄氏度 to 华摄氏度")  # 询问玩家要进行哪种转换，通过输入数字的方式进行
choice = input("请输入序号：") 
if choice == '1':
    Fahrenheit = input("请输入华摄氏度：")
    if float(Fahrenheit) < -459.67:  # 以防出现绝对零度的出现
        print("该温度低于绝对零度，程序结束")
    elif float(Fahrenheit) > 100000:  # 设立一个上限没有特别意义
        print("你输入的数值过大，程序结束")
    else:
        Celsius_Result = (float(Fahrenheit) - 32) / 1.8
        print(str(round(Celsius_Result,2))+"摄氏度")  # 用round取小数的方式不是最普遍的似乎
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
