def count_items(values):
    types = {}
    for typ in values:
        types[typ] = types.get(typ, 0) + 1 #проверяет если в словаре такой тип, если нет, то создаёт, и даём ему значение 0, и прибавляет 1
    return types

def unique_sorted(values):
    res = []
    for typ in values:
        res.append(typ)
    return sorted(set(res))

def common(first, second):
    res = []
    for typ in first:
        if typ in second:
            res.append(typ)

    return sorted(res)

def only_in_first(first, second):
    res = []
    for typ in first:
        if typ not in second:
            res.append(typ)

    return res