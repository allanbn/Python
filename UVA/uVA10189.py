import sys

def init():
    matrix = []
    for i in range(101):
        llista = []
        for j in range(101):
            llista.append(-1)
        matrix.append(llista)
    return matrix


matrix = init()

while True:
    for line in sys.stdin:
        line.rstrip()
        line.split()
        n = int(line[0])
        m = int(line[2])
        for i in range(n):
                string = input()
                for j in range(m):
                    matrix[i][j] = string[j] 
        #print(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "*":
                    print("*", end="")
                else:
                    count = 0
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            if matrix[x][y] == "*":
                                count += 1
                        print("{}".format(count), end="")