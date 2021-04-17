def main(y, w):
    greater = max(y, w)
    rem = (6 - greater) + 1
    if rem % 6 == 0:
        print(f"{(rem // 6)}/{(6 // 6)}")
    elif rem % 2 == 0:
        print(f"{(rem // 2)}/{(6 // 2)}")
    elif rem % 3 == 0:
        print(f"{(rem // 3)}/{(6 // 3)}")
    else:
        print(f"{rem}/{6}")


if __name__ == '__main__':
    y, w = map(int, input().split())
    main(y, w)
