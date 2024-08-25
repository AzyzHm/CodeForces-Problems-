def count_sheets(n):
    count = 1
    while n % 2 == 0:
        count *= 2
        n //= 2
    return count

def main():
    t = int(input())
    results = []
    for _ in range(t):
        w, h, n = map(int, input().split())
        total_sheets = count_sheets(w) * count_sheets(h)
        if total_sheets >= n:
            results.append("YES")
        else:
            results.append("NO")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
