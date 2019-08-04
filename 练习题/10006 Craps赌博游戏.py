"""
Craps赌博游戏
- 玩家掷骰子，点数为1到6
- 如果第一次点数和为7或11，则玩家胜
- 如果点数和为2、3或12，则玩家输
- 如果和为其他点数，则记录第一次的点数和，然后继续掷骰子
- 如果掷出了第一次的点数和，则玩家胜
- 如果在这之前掷出了7，则玩家输
Author: 蓝为一
Date: 2019年8月3日
"""
import random
input("键入任意数字投掷第一个骰子：")
a = random.randint(1, 6)
print("第一个骰子为："+str(a))
input("键入任意数字投掷第二个骰子：")
b = random.randint(1, 6)
print("第二个骰子为："+str(b))
print("两次骰子之和为："+str(a+b))
if a+b == 7 or a+b == 11:
    print("点数和为7，你胜利啦！")
elif a+b == 2 or a+b == 3 or a+b == 12:
    print("点数和为2、3或12，你输啦！")
else:
    print("点数和不是2、3、7、11、12中的一个，你需要继续投掷\n如果投掷的和为"+str(a+b)+"你将获胜。\n如果和为7，则你输了。\n")
    for n in range(1, 100):
        input("键入任意数字投掷第一个骰子：")
        c = random.randint(1, 6)
        print("第一个骰子为：" + str(c))
        input("键入任意数字投掷第二个骰子：")
        d = random.randint(1, 6)
        print("第二个骰子为：" + str(d))
        print("两次骰子之和为：" + str(c + d))
        if c+d == a+b:
            print("你胜利啦！")
            break
        elif c+d == 7:
            print("你输啦！")
            break
        else:
            print("两个骰子之和不为"+str(a+b)+"或7，你需要再投掷1次\n")
            continue
