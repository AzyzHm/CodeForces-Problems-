def main():
    t = int(input())
    results = []
    for i in range(t):
        a = list(map(int,input().split()))
        a.sort()
        results.append(a)
    for result in results:
        print(*result)

if __name__ == "__main__":
    main()