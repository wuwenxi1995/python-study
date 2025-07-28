import numpy as np


# a = np.arange(15).reshape(3,5)
#
# print(a)
# print(a.shape)
# print(a.itemsize)
# print(a.size)

# print('*'*5)
# print('*'*5)
# print('*'*5)
# print('*'*5)
# print('*'*5)
#
# a = 1
# b = 2
# a,b = b,a
# print("a:",a,"b:",b)

def check_bounds(c):
    return c[0] % 9 == c[0] and c[1] % 9 == c[1]


c = (0, 2)
dic = {c}

print(dic)

coordinates = [(i, j) for i in range(9) for j in range(9)]
neighbors = {(x, y): list(filter(check_bounds, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])) for
             x, y in coordinates}
print(coordinates)
print(neighbors)

empty_board = np.zeros([9, 9], dtype=np.int8)
print("empty_board", empty_board)
empty_board[(0, 2)] = 1
print(empty_board[(0, 2)])


# board = np.ones([9, 9], dtype=np.int8)

# frontier = [c]
# while frontier:
#     current = frontier.pop()
#     print('current', current)
#     for n in neighbors[current]:
#         print("", n, board[n])

def find_reached(board, x):
    color = board[x]
    chain = {x}
    reached = set()
    frontier = [x]
    '''
        1.循环从frontier取出第一个坐标
            1.如果相邻点棋子颜色一致并且并没有在棋组中, 将当前坐标加入到frontier尾部
            2.如果相邻点与当前棋组颜色不一致, 则加入到reached集合中
        2. 如果frontier为空结束查询

        例如board:
        [[0,1,-1,0],
         [-1,1,1,-1],
         [-1,0,1,0],
         [0,-1,1,1]]
        查询(0,2)位置的相邻信息
        chain输出: {(0,2),(1,2),(1,3),(2,2),(3,2),(3,3)}
        reached输出: [(0,0),(0,2),(1,0),(1,3),(2,1),(2,3),(3,1)]

    '''
    while frontier:
        current = frontier.pop()
        chain.add(current)
        for n in neighbors[current]:
            if board[n] == color and n not in chain:
                frontier.append(n)
            # 如果颜色不一致, 加入到reached用于计算气
            elif board[n] != color:
                reached.add(n)
    return chain, reached


board = {}
for x in range(0, 9):
    for y in range(0, 9):
        if x < 3 and (x == 1 or y == 1):
            board[(x, y)] = 1
        else:
            board[x, y] = 0

print(board)

chain, reached = find_reached(board, (0, 1))
print('chain', chain)
print('reached', reached)
