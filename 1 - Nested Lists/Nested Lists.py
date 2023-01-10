# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# if __name__ == '__main__':
#     mydic = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         mydic[name] = score
#
# mydic_sorted = sorted(mydic.items(), key= lambda x: x[1])
# lowest = next(iter(mydic_sorted))
# lowest_key = mydic_sorted.pop(lowest)
#
# print(mydic_sorted)

# Solution:

# if __name__ == '__main__':
#     dict_a = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         dict_a[name] = score
#     values=sorted(list(set(dict_a.values())))
#     lst = []
#     for key, value in dict_a.items():
#         if values[1] == value:
#             lst.append(key)
#     lst.sort()
#     for items in lst:
#         print(items)

dict_a = {}
for _ in range(int(input())):
        name = input()
        score = float(input())
        dict_a[name] = score
values=sorted(list(set(dict_a.values())))
lst = []
for key, value in dict_a.items():
        if values[1] == value:
            lst.append(key)
lst.sort()
for items in lst:
        print(items)
