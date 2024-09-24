def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        s = 0
        for i in range(n):
            if a[i] < 0:
                s -= a[i]
            else:
                s += a[i]
        results.append(s)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()