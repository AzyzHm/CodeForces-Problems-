def solve(n,x):
    num = 0
    for i in range(1, n+1):
        pass
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,x = map(int, input().split())
        results.append(solve(n,x))
    for r in results:
        print(r)

if __name__ == '__main__':
    main()