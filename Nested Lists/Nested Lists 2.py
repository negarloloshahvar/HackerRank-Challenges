records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

records.sort(key= lambda item: (item[1], item[0]))
print(records)

