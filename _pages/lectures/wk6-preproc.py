records = []
with open('wk6-basic-io.txt') as f:
    next(f)
    for line in f.readlines():
        info = line.split(',')
        records.append(tuple(info[1:4]))

records = sorted(records)
print(records)

with open('baseball.txt', 'w') as f:
    for rec in records:
        f.write(",".join(rec) + "\n")