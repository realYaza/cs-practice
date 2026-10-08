
def winner(names, scores):
    mx = [-9999999999, 0]
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
    return float(f'{(sum / i):.3}')

def ranking(names, scores):
    ns = []
    res = []
    for i in range(len(names)):
        ns.append((names[i], scores[i]))

    ns = sorted(ns, key = lambda x: -x[1])

    for obj in ns:
        res.append(obj[0])

    return res

def above_average(names, scores):
    av = average(scores)
    res = []

    for i in range(len(names)):
        if scores[i] > av:
            res.append(names[i])
    return res
