# solution incomplete
def solve(n, a):
    a.sort()
    operations = []
    while len(operations) <= 40:
        if sum(a) == 0:
            return "\n".join(map(str, [len(operations), " ".join(map(str, operations))]))
        else:
            x = max(a)
            a = list(map(lambda e: abs(e - x), a))
            operations.append(x)
    
    return -1

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
