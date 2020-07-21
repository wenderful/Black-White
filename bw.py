user1 = '@'
user2 = 'O'
a = 8
b = 8
def display(squrd):
    col_label = 'a'
    x = len(squrd)
    print("\r ")
    for col in range(x):
        print("   " + chr(ord(col_label) + col),end = "")
    print("\r")

    for row in range(x):
        print(" +",end="")
        for col in range(x):
            print("---+",end="")
        print("\n" + str(row + 1) + "|", end="")
        for col in range(x):
#            print(squrd[row][col])
            print(' {} |'.format(squrd[row][col]), end="")
        print("\r")

    print(" +",end="")
    for col in range(x):
        print("---+",end="")
    print("\r")

def reset(squrd):
    x = len(squrd)
    for row in range(x):
        for col in range(x):
            squrd[row][col] = ' '
    mid = x//2
    squrd[mid-1][mid-1] = squrd[mid][mid] = user1
    squrd[mid-1][mid] = squrd[mid][mid-1] = user2
    return squrd

def validmoves(squrd,moves,player):
    s = len(squrd)
    no_of_moves = 0
    other_player = user2 if player == user1 else user1

    for row in range(s):
        for col in range(s):
            moves[row][col] = False

    for row in range(s):
        for col in range(s):
            if squrd[row][col] != ' ':
                continue
            for row_m in range(-1,2):
                for col_m in range(-1,2):
                    if row == 0 and row_m ==-1 or (row + row_m) > (s - 1) or col == 0 and col_m == -1 or (col + col_m) > (s - 1):
                        continue
                    if squrd[row + row_m][col + col_m] == other_player:
                        x = row + row_m
                        y = col + col_m
                        while True:
                            x +=row_m
                            y +=col_m
                            if x < 0 or x >= s or y < 0 or y >= s or squrd[x][y] == ' ':
                                break
                            if squrd[x][y] == player:
                                moves[row][col] = True
                                no_of_moves += 1
                                break
    return no_of_moves

def make_moves(squrd,row,col,player):
    row_m = 0
    col_m = 0
    s = len(squrd)
    other_player = user2 if player == user1 else user1
    squrd[row][col] = player

    for row_m in range(-1,2):
        for col_m in range(-1,2):
            if row == 0 and row_m == -1 or (row + row_m) > (s - 1) or col == 0 and col_m == -1 or (col + col_m) > (
                    s - 1) or row_m == 0 and col_m == 0:
                continue
            if squrd[row + row_m][col + col_m] == other_player:
                x = row + row_m
                y = col + col_m

                while True:
                    x += row_m
                    y += col_m
                    if x >= s-1 or y >= s-1 or x <= 0 or y <= 0 or squrd[x][y] == ' ':
                        break
                    if squrd[x][y] == player:
                        while True:
                            x -= row_m
                            y -= col_m
                            if squrd[x][y] == other_player:
                                squrd[x][y] = player
                            elif squrd[x][y] == player:
                                break
                        break
    return squrd



def computer_moves():
    pass

def counters(squrd,player):
    l = len(squrd)
    count = 0
    for row in range(l):
        for col in range(l):
            if(squrd[row][col] == player):
                count += 1
    return count


def main():
    squrd = [[' ' for i in range(8)] for j in range(8)]
    moves = [[False for i in range(8)] for j in range(8)]
    no_of_moves = 0
    invalid_moves = 0
    again = 0
    next_player = True
    s = len(squrd)

    while True:
        reset(squrd)
        display(squrd)
        while True:
            next_player = not next_player
            no_of_moves = 4
            if next_player == True:
                if validmoves(squrd,moves,user1):
                    while True:
                        x,y = [i for i in input("@请输入（行+列，中间没有空格）！")]
                        y = ord(y.lower()) - ord('a')
                        x = int(x) - 1
                        if y < 0 or y >= s - 1 or x >= s - 1 or not moves[x][y]:
                            print("不是有效的位置，请重试！")
                            continue
                        make_moves(squrd,x,y,user1)
                        display(squrd)
                        no_of_moves += 1
                        break
                else:
                    invalid_moves += 1
                    if invalid_moves < 2:
                        again = input("这一步不能走，是否重试(y/n)？")
                    else:
                        print("没有步可以走了，游戏结束")
            else:
                if validmoves(squrd,moves,user2):
                    while True:
                        x,y = [i for i in input("O请输入（行+列，中间没有空格）！")]
                        y = ord(y.lower()) - ord('a')
                        x = int(x) - 1
                        if y < 0 or y >= s - 1 or x >= s - 1 or not moves[x][y]:
                            print("不是有效的位置，请重试！")
                            continue
                        squrd = make_moves(squrd,x,y,user2)
                        display(squrd)
                        no_of_moves += 1
                        break
                else:
                    invalid_moves += 1
                    if invalid_moves < 2:
                        again = input("这一步不能走，按回车跳过")
                    else:
                        print("没有步可以走了，游戏结束")
            if no_of_moves > s * s and invalid_moves >=2:
                break

        display(squrd)
        print("最终分数是:")
        print("user1的分数是{},user2的分数是{}".format(counters(squrd,user1),counters(squrd,user2)))
        again = input("还想玩吗(y/n):")
        if again.lower() == 'n':
            break

if __name__ == main():
    main()


#b = [[' ' for i in range(8)] for j in range(8)]
#m = [[' ' for i in range(8)] for j in range(8)]
#display(make_moves(reset(b),4,5,'O'))
#display(reset(b))
#print(validmoves(reset(b),m,user1))
