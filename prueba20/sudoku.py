def verificar(T, r, c, v):
    i = 0

def sudoku(T, r, c):
    ans = None
    if r == 9:
        return ans
    elif c == 9:
        sudoku(T, r + 1, 0)
    else:
        if T[r][c] != 0:
            if verificar(T, r, c, T[r][c]) == False:
                ans = sudoku(T, r, c + 1)
            else:
                ans = False
        else:
            v = 1
            ans = False
            while ans == False and v != 10:
                if verificar(T, v, r, v) == False:
                    T[r][c] = v
                    sudoku(T, r, c + 1)
                v += 1
            if ans == False:
                T[r][c] = 0
    return ans
    

def main(args):
    T = []
    for n in range(9):
        tmp = []
        for m in range(17):
            if args[n][m] != " ":
                tmp.append(int(args[n][m]))
        T.append(tmp)
    print(T)

main()