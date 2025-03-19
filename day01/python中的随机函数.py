# 导入包下面全部方法
# import random
# 导入指定包下面的方法
from random import randint as r

while True:
    player = int(input("请输入出拳信息的(石头-1, 剪刀-2, 布-3):"))
    if player < 1 or player > 3:
        print("不符合规则, 请重新输入[1-3]的数字(石头-1, 剪刀-2, 布-3)")
        continue
    compute = r(1, 3)
    print(player, compute, sep=',')
    if player == compute:
        print("平局, 请继续")
        continue
    elif (player == 1 and compute == 2) or (player == 2 and compute == 3) or (player == 3 and compute == 1):
        print("玩家胜利")
    else:
        print("电脑胜利")
    break
