def solver(n,x):
    if n <= 2:
        return 1
    n -= 2
    return (n + x - 1) // x + 1
def main():
    t = int(input())
    resuults = []
    for _ in range(t):
        n,x = map(int, input().split())
        resuults.append(solver(n,x))
    for res in resuults:
        print(res)

if __name__ == '__main__':
    main()