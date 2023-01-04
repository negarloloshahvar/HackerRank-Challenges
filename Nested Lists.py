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
