import sys


# n, x, k = [int(s) for s in sys.stdin.readline().strip().split(' ')]
# alarms_clock = [int(s) for s in sys.stdin.readline().strip().split(' ')]

# n, x, k = 5, 7, 12
# alarms_clock = sorted([5, 22, 17, 13, 8])

n, x, k = 6, 5, 10
alarms_clock = sorted([1, 2, 3, 4, 5, 6])
alarms = []
clock_index = 0
j = 0
flag_continue_calc = True

while flag_continue_calc:
    flag_continue_calc = False
    for i in alarms_clock:
        clock = i + j * x
        if len(alarms) < k:
            if not alarms.count(clock):
                alarms.append(clock)
            flag_continue_calc = True
            continue
        max_clock = max(alarms)
        if clock < max_clock:
            if not alarms.count(clock):
                alarms[alarms.index(max_clock)] = clock
            flag_continue_calc = True
        else:
            break
    j += 1

print(sorted(alarms)[k-1], sorted(alarms))