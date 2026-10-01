print('Ввод:')
porog = float(input())
n = int(input())
er_count = 0
prv_count = 0
max_value = 0
sum = 0

for i in range(n):
    zap = input()
    if zap != 'error':
        zap = float(zap)

        if zap > porog:
            prv_count += 1
        sum += zap
        max_value = max(max_value, zap)
    else:
        er_count += 1
