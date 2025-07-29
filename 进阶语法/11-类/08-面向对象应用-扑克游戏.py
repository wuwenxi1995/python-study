# -*- coding: utf-8 -*-
# @Time    : 2025/7/29 21:45
# @Author  : wuwenxi

import random
from enum import Enum

"""
简单起见，我们的扑克只有52张牌，游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
"""

"""
    花色
"""


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND, JOKER = range(5)


"""
    牌, 花色+点数
"""


class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suite = '♠♥♣♦'
        faces = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        joker = ['小王', '大王']
        return f'{joker[self.face]}' if self.suite.value > 3 else f'{suite[self.suite.value]}{faces[self.face]}'

    '''
        重写__lt__方法, 主要目的比较对象大小
    '''

    def __lt__(self, other):
        if self.suite == Suite.JOKER and other.suite != Suite.JOKER:
            return False
        elif other.suite == Suite.JOKER and self.suite != Suite.JOKER:
            return True
        elif self.suite == other.suite == Suite.JOKER:
            return self.face < other.face
        # 花色一致比点数否则比颜色
        return self.suite.value < other.suite.value if self.face == other.face else self.face < other.face


"""
牌组
"""


class Poker:
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite if suite.value < 4 for face in range(13)]
        for j in range(2):
            self.cards.append(Card(Suite.JOKER, j))
        self.index = 0
        self.shuffle()

    '''
        打乱排序
    '''

    def shuffle(self):
        self.index = 0
        random.shuffle(self.cards)

    def next(self):
        card = self.cards[self.index]
        self.index += 1
        return card

    def has_next(self):
        return self.index < len(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.cards: list[Card] = []

    def append(self, card):
        self.cards.append(card)

    def arrange(self):
        return self.cards.sort()


# 生成棋牌
poker = Poker()
# 打乱排序
poker.shuffle()
players = [Player('赵四'), Player('王五'), Player('张三')]

common = Player('底牌')
for _ in range(3):
    common.append(poker.next())

# 每个人发17张
for _ in range(17):
    for p in players:
        if poker.has_next():
            p.append(poker.next())

print(f'底牌:{common.cards}')

# 打印每个人手上的牌
for player in players:
    # 先将手牌排序
    player.arrange()
    print(f'当前玩家: {player.name}', end=' ')
    print(player.cards)
