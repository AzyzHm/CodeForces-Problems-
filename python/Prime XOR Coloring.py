# solution incomplete
def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def solve(n):
    solution = []
    i = 1
    while len(solution) < n:
        if i == 1:
            solution.append(1)
            i+=1
        else:
            solution.append(i)
            solution.append(i)
            if len(solution) > n:
                solution.pop()
                break
            i+=1
    x = " ".join(map(str,solution))
    return "\n".join([str(solution[-1]), x])
            
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(solve(n))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()