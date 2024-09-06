def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        if n % 2 == 1:
            results.append(n // 2)
        else:
            results.append(n // 2 - 1)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()