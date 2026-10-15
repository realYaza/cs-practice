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


path = 'events.csv'

with open(path, encoding = "utf-8") as table:
    rows = read_rows(table)

with open("summary.csv", "w", encoding="utf-8") as out:
    types = len(count_types(rows))
    er_sum= total_minutes(rows, 'ошибка')

    out.write(f'{len(rows)}' + '\n' + f'{types}' + '\n' + f'{er_sum}')