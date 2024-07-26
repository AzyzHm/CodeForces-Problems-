def solve(n, k, a):
    solution = ""
    for i in range(n):
        if i%k == 0:
            for j in range(n):
                if j%k == 0:
                    solution += a[i][j]
            if i != n-k:
                solution += "\n"
        else:
            continue
    return solution
def main():
    t = int(input())
    results = []
    for _ in range(t):
        a = []
        n,k = map(int, input().split())
        for _ in range(n):
            a.append(list(input()))
        results.append(solve(n,k,a))
    for r in results:
        print(r)
if __name__ == '__main__':
    main()