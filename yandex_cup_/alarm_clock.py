import sys


# n, x, k = [int(s) for s in sys.stdin.readline().strip().split(' ')]
# alarms_clock = [int(s) for s in sys.stdin.readline().strip().split(' ')]

# n, x, k = 5, 7, 12
# alarms_clock = sorted([5, 22, 17, 13, 8])

n, x, k = 6, 5, 10
alarms_clock = sorted([1, 2, 3, 4, 5, 6])

for i in range(n):
    for j in range(i+1, n):
        if alarms_clock[i] % x == alarms_clock[j] % x:
            alarms_clock[j] = 0
alarms_clock = list(filter(lambda num: num != 0, alarms_clock))
# https://temofeev.ru/info/articles/razbor-kvalifikatsii-chempionata-po-programmirovaniyu-sredi-bekend-razrabotchikov/
k_max = 0
t = 0
while k_max < k:
    k_max = sum([int((t - i) / x) for i in alarms_clock])
    t += 1

print(t-1, alarms_clock)
exit()
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