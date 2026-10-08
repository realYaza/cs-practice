
def winner(names, scores):
    mx = [-1, 0]
    i = 0
    for sc in scores:
        if sc > mx[0]:
            mx = [sc, i]
        i += 1
    return names[mx[1]]
