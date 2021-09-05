import sys

k, n = [int(i) for i in sys.stdin.readline().strip().split(' ')]
m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
vasya = 0
petya = 0
for i in m:
    if i % 5 == 0 and i % 3 != 0:
        vasya += 1
    elif i % 3 == 0 and i % 5 != 0:
        petya += 1
    if vasya == k or petya == k:
        break

if vasya > petya:
    print('Vasya')
elif petya > vasya:
    print('Petya')
else:
    print('Draw')