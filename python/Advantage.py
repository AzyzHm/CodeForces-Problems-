def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        sorted_s = sorted(s, reverse=True)
        best = sorted_s[0]
        second_best = sorted_s[1]
        diff = []
        for participant in s:
            if participant == best:
                diff.append(participant - second_best)
            else:
                diff.append(participant - best)
        results.append(diff)
    for result in results:
        print(*result)

if __name__ == '__main__':
    main()