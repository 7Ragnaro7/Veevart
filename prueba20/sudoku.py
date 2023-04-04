def verificar(T, r, c, v):
    i = 0
    ans = False
    T[r][c] = 0
    while ans == False and i != 9:
        if T[r][i] == v or T[i][c] == v:
            ans = True
        else:
            ans = False
        i += 1
    i = 0
    rr = (r // 3) * 3
    cc = (c // 3) * 3
    while ans == False and i != 3:
        j = 0
        while ans == False and j != 3:
            if T[rr + i][cc + j] == v:
                ans = True
            else:
                ans = False
            j += 1
        i += 1
    T[r][c] = v
    return ans

def sudoku(T, r, c):
    ans = None
    if r == 9:
        ans  = True
    elif c == 9:
        ans = sudoku(T, r + 1, 0)
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
                if verificar(T, r, c, v) == False:
                    T[r][c] = v
                    ans = sudoku(T, r, c + 1)
                v += 1
            if ans == False:
                T[r][c] = 0
    return ans
    

def main():
    T = ["5 3 0 0 7 0 0 0 0", "6 0 0 1 9 5 0 0 0", "0 9 8 0 0 0 0 6 0", "8 0 0 0 6 0 0 0 3", "4 0 0 8 0 3 0 0 1", "7 0 0 0 2 0 0 0 6", "0 6 0 0 0 0 2 8 0", "0 0 0 4 1 9 0 0 5", "0 0 0 0 8 0 0 7 9"]
    tablero = []
    for n in range(9):
        tmp = []
        for m in range(17):
            if T[n][m] != " ":
                tmp.append(int(T[n][m]))
        tablero.append(tmp)
    if(sudoku(tablero, 0, 0)):
        print(tablero)
    else:
        print("El sudoku no tiene solucion")

main()