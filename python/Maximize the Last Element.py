def solve(n,a):
    maxes = []
    for i in range(n):
        if i % 2 == 0:
            maxes.append(a[i])
    return max(maxes)
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(solve(n, a))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()