def main():
    t = int(input())
    results = []
    for _ in range(t):
        a, b = map(int, input().split())
        if a == 0:
            results.append(1)
        else:
            results.append(a + 2 * b + 1)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()