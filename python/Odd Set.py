def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if len(a) == 2 * n:
            odd_count = sum(1 for num in a if num % 2 == 1)
            if odd_count == n:
                results.append("Yes")
            else:
                results.append("No")
        else:
            results.append("No")
    for result in results:
        print(result)

if __name__ == '__main__':
    main()