def read_rows(lines):
    headers = []
    res = []
    for line in lines:
        line = line.strip().split(',')
        if line != '':
            if len(headers) == 0:
                headers = [line[0], line[1], line[2]]
            elif len(line) == len(headers):
                res.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2]})

    return res


def count_types(rows):
    types = {}
    for row in rows:
        type = row['тип']
        types[type] = types.get(type, 0) + 1

    return types


def total_minutes(rows, kind):
    cnt = 0
    for row in rows:
        if row["тип"] == kind:
            cnt += float(row['минуты'].replace(',', '.'))

    return round(cnt, 1)

def to_csv(counts):
    res = sorted( [(key, value) for key, value in counts.items()] )
    lines = ['тип, количество']
    for q in res:
        lines.append(f'{q[0]}, {q[1]}')

    return '\n'.join(lines) + '\n'