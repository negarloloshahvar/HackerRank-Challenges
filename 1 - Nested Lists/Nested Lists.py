records = []

for i in range(int(input('N= '))):
    name = input('Name= ')
    score = int(input('Score= '))
    records.append([name, score])

records.sort(key= lambda item: (item[1], item[0]))

print(records)

lowest = second_lowest = records[0][1]
value_update = 0
i = 0
size = len(records)

while i < size:
    if records[i][1] > second_lowest:
        second_lowest = records[i][1]
        value_update += 1
    if value_update == 1:
        print(records[i][0])
    if lowest != second_lowest and value_update > 2:
        break
    i += 1