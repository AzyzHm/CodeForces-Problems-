def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        b = input()
        if len(set(sorted(b))) == 1:
            results.append(0)
        else:
            indexes = [s.index(char) + 1 for char in b]
            n = len(indexes)
            res = 0
            for i in range(n):
                if i == 0:
                    continue
                else:
                    res += abs(indexes[i] - indexes [i-1])
            results.append(res)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()