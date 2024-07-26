def solve(n):
    return n // 4 + (n - 4*(n//4)) // 2
    
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(solve(n))
    for r in results:
        print(r)
        

if __name__ == '__main__':
    main()