def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        if a[-1] <= d or a[0] + a[1] <= d:
            results.append("YES")
        else:
            results.append("NO")
    for result in results:
        print(result)

if __name__ == '__main__':
    main()