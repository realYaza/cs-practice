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