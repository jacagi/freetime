cols = 9
numbers = [i for i in range(1, 10)]
columnas = []
filas = []
sectores = []

def getoptions(sudoku):
    global filas, columnas, sectores
    for i in range(0, cols):
        for j in range(0, cols):
            if sudoku[i][j] != 0:
                filas[i].append(sudoku[i][j])
                columnas[j].append(sudoku[i][j])
                if i < 3:
                    if j < 3:
                        sectores[0].append(sudoku[i][j])
                    elif 2 < j < 6:
                        sectores[1].append(sudoku[i][j])
                    else:
                        sectores[2].append(sudoku[i][j])
                elif 2 < i < 6:
                    if j < 3:
                        sectores[3].append(sudoku[i][j])
                    elif 2 < j < 6:
                        sectores[4].append(sudoku[i][j])
                    else:
                        sectores[5].append(sudoku[i][j])
                else:
                    if j < 3:
                        sectores[6].append(sudoku[i][j])
                    elif 2 < j < 6:
                        sectores[7].append(sudoku[i][j])
                    else:
                        sectores[8].append(sudoku[i][j])
    filas = list(set(numbers) - set(filas))
    columnas = list(set(numbers) - set(columnas))
    sectores = list(set(numbers) - set(sectores))
def readinput():
    f = open("input.txt", "r")
    sudoku = []
    for l in f:
        line = []
        l = l.replace("\n", "")
        for n in l:
            line.append(n)
        sudoku.append(line)
    print(sudoku)
    return sudoku

def initbacktrack(sudoku, i, j):
    if j == 9:
        j = 0
        i += 1
    if sudoku[i][j] == 0:
        if not filas[i]:
            sudoku[i][j] = filas.pop(0)
        elif not columnas[i]:
            sudoku[i][j] = columnas.pop(0)
        elif not sectores[i]:
            sudoku[i][j] = sectores.pop(0)
        else:
            print("xD")
    else:
        j += 1
        initbacktrack(sudoku, i, j)


def main():
    sudoku = readinput()
    getoptions(sudoku)
    initbacktrack(sudoku, 0, 0)


if __name__ == '__main__':
    main()
