
def winner(names, scores):
    mx = [-1, 0]
    i = 0
    for sc in scores:
        if sc > mx[0]:
            mx = [sc, i]
        i += 1
    return names[mx[1]]

def average(scores):
    sum = 0
    i = 0
    for sc in scores:
        sum += sc
        i += 1

    if i == 0:
        return 0.0
    return sum / i
