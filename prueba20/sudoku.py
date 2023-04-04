#funcion verificar que se encarga de decir si el numero en la casilla del tablero[r][c]
#es correcta
def verificar(T, r, c, v):
    i = 0
    ans = False
    T[r][c] = 0
    #Revisamos sobre toda la fila y sobre toda la columna si el numero se encuentra
    while ans == False and i != 9:
        if T[r][i] == v or T[i][c] == v:
            ans = True
        else:
            ans = False
        i += 1
    #rr y cc son variables que indican en que de los 9 cuadros me encuentro
    i = 0
    rr = (r // 3) * 3
    cc = (c // 3) * 3
    #y hacemos el recorrido sobre dicho cuadro del sudoku para verificar si se encuentra el valor
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


#Funcion recursiva que resuelve el problema de sudoku
#recibe como parametros el tablero, la fila y la columna

def sudoku(T, r, c):
    ans = None
    #Caso base | si llegamos a la ultima fila es porque encontramos una solucion al problema
    if r == 9:
        ans  = True
    #Primer caso inductivo | si no terminamos las filas pero si las columnas, pasamos a la 
    #sgte fila y reseteamos las columnas a 0
    elif c == 9:
        ans = sudoku(T, r + 1, 0)
    #Segundo caso inductivo | Si no ha terminado ni filas ni columnas entonces tenemos dos opciones
    #cuando en el tablero en la fila r y columna c tenga un 0 o cuando tenga un valor entre 1-9
    else:
        #Si el tablero tiene un numero entre 1-9 entonces
        if T[r][c] != 0:
            #Pasamos a la el tablero, fila, columna y valor a la funcion verificar
            #que se encarga de revisar si el numero que se encuentra en esa posicion
            #es valido en el tablero, si retorna false es porque si esta bien y continua
            #en el siguiente llamado de backtracking columna + 1
            if verificar(T, r, c, T[r][c]) == False:
                ans = sudoku(T, r, c + 1)
            #de lo contrario esta malo
            else:
                ans = False
        #Si el valor es 0 debemos ver que numero colocar
        else:
            #inicializar una var v para llevar el numero entre 1-9 y ans en falso para verificar
            v = 1
            ans = False
            while ans == False and v != 10:
                #Volvemos a usar la funcion verificar y hacemos el llamado con la var v
                #si entra en el if marcamos en el tablero en la fila y columna el valor de v y
                #seguimos en el backtrack
                if verificar(T, r, c, v) == False:
                    T[r][c] = v
                    ans = sudoku(T, r, c + 1)
                v += 1
            #reiniciar el valor para otras ramas del backtrack
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