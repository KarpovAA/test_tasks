import sys

n = int(sys.stdin.readline())
start = 0
finish = n
i = delta = n // 2
b = None

while True:
    sys.stdout.write(str(i))
    a = int(sys.stdin.readline())
    sys.stdout.flush()

    if delta == 1:
        if a == 0 and b == 1:
            print('!', i)
            break
        elif b == 0 and a == 1:
            print('!', b_n)
            break

    if a == 1:
        start = i
        delta = (finish - start) // 2 or 1
        i += delta
    else:
        finish = i
        delta = (finish - start) // 2 or 1
        i -= delta
    b = a
    b_n = i