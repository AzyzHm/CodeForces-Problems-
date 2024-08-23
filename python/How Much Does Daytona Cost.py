def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        if a.count(k) > 0:
            results.append("Yes")
        else:
            results.append("No")
    for result in results:
        print(result)

if __name__ == '__main__':
    main()