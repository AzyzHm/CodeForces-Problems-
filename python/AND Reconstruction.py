# solution incomplete
def solve(n,b):
    solution = []
    pass
        
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        results.append(solve(n, b))
    for result in results:
        print(result)
        
if __name__ == "__main__":
    main()