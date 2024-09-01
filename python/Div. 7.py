def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        if n % 7 == 0:
            results.append(n)
        else:
            rest = n % 7
            if n % 10 > rest:
                results.append(n - rest)
            else:
                results.append(n + 7 - rest)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()