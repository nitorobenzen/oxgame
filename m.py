from random import randint
BOARD = 3
board = []
win = 0
for n in range(BOARD):
    board.append([])
    for i in range(BOARD):
        board[n].append(0)

def show():
    for i in range(BOARD):
        print(board[i])

def main():
    win = 0
    show()
    print()
    u = input("なんの何番目？")# 2の3番目は23
    user = list(u)
    if user[0] == "exit" or user[0] == "e":
        return False
    
    if board[int(user[0])-1][int(user[1])-1] == 1 or board[int(user[0])-1][int(user[1])-1] == 2:
        print("そこにはすでにあります")
        main()
    board[int(user[0])-1][int(user[1])-1] = 1
    show()
    for i in range(BOARD):
        if board[i][i] == 1:
            win = win + 1
    if win == BOARD:
        print("貴方の勝ち!")
    win = 0
    for i in range(BOARD):
        if board[i][-(i + 1)] == 1:
            win = win + 1
    if win == BOARD:
        print("貴方の勝ち!")
        win = 0
    for n in range(BOARD):
        for i in range(BOARD):
            if board[i][n] == 1:
                win = win + 1
        if win == BOARD:
            print("貴方の勝ち!")
        win = 0
    for n in range(BOARD):
        for i in range(BOARD):
            if board[n][i] == 1:
                win = win + 1
        if win == BOARD:
            print("貴方の勝ち!")
        win = 0
    print()
    com_hand()
    show()
    print()

def com_hand():
    win = 0
    com = randint(0,(BOARD - 1))
    com2 = randint(0,(BOARD - 1))
    if board[com][com2] == 2 or board[com][com2] == 1:
        com_hand()
        return
    board[com][com2] = 2
    for i in range(BOARD):
        if board[i][i] == 2:
            win = win + 1
    if win == BOARD:
        print("貴方の負け...")
    win = 0
    for i in range(BOARD):
        if board[i][-(i + 1)] == 2:
            win = win + 1
    if win == BOARD:
        print("貴方の負け...")
        win = 0
    for n in range(BOARD):
        for i in range(BOARD):
            if board[i][n] == 2:
                win = win + 1
        if win == BOARD:
            print("貴方の負け...")
        win = 0
    for n in range(BOARD):
        for i in range(BOARD):
            if board[n][i] == 2:
                win = win + 1
        if win == BOARD:
            print("貴方の負け...")
        win = 0

while True:
    main()
    flag = main()
    if flag == False:
        print("終了します")
        break