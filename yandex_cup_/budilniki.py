import sys


n, x, k = [int(s) for s in sys.stdin.readline().strip().split(' ')]
alarms_clock = [int(s) for s in sys.stdin.readline().strip().split(' ')]
alarms = []
max_clock = 0

for i in alarms_clock:
    j = 0
    while True:
        clock = i + j * x
        if len(alarms) < k:
            alarms.append(clock)
            max_clock = clock
        elif max_clock > clock:
            if not alarms.count(clock):
                alarms[alarms.index(max(alarms))] = clock
        else:
            break
        j += 1

result = sorted(alarms)

print(result[k-1])
