n = int(input())
if n % 2 == 0:
    print(n//2)
    print('2 ' * (n//2))
else:
    n = n - 3
    print(n//2 + 1)
    print('2 ' * (n//2) + '3')
