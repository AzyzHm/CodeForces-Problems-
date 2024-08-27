def main():
    t = int(input())
    problems = ['A', 'B', 'C', 'D', 'E', 'F','G']
    results = []
    for _ in range(t):
        n,m = map(int,input().split())
        p = input()
        counts = [m - p.count(i) for i in problems]
        count = 0
        for i in counts:
            if i > 0:
                count += i
        results.append(count)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()