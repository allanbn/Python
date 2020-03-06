import sys

def sol(arr):
    return

n = 999
while n > 0:
    n = int(input())
    arr_lul = []
    while (len(arr_lul) < n):
        arr = sys.stdin.readlines() # takes the whole line of n numbers
        print(arr)
        for i in arr:
            i = i.replace("\n", "")
            i = i.split(" ")
            print(i)
            for j in i:
                arr_lul.append(int(j))
        print(arr_lul)
    arr_lul.clear()
# lines = sys.stdin.readlines()
# for i in range(len(lines)):
#     lines[i] = lines[i].rstrip()


# # for line in sys.stdin:
# #     print(line)