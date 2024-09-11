def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        minimum = min(a)
        maximum = max(a)
        results.append(maximum - minimum)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()