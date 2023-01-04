# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    mydic = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mydic[name] = score

mydic_sorted = sorted(mydic.items(), key= lambda x: x[1])
lowest = next(iter(mydic_sorted))
lowest_key = mydic_sorted.pop(lowest)

print(mydic_sorted)
