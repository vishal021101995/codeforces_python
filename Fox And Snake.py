row, col = map(int, input().split())
for i in range(1, row+1):
    if i % 2 == 0 and i % 4 != 0:
        print('.' * (col - 1) + "#")
    elif i % 4 == 0:
        print("#" + '.' * (col - 1))
    else:
        print('#' * col)
