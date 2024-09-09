def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        for number in a:
            if a.count(number) == 1:
                results.append(a.index(number) + 1)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()