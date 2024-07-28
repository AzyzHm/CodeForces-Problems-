def solve(n, a):
    a.sort()
    a[0] += 1
    result = a[0]
    for i in range(1, n):
        result *= a[i]
    return result
    
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