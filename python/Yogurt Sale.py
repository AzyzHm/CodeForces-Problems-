def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,a,b = map(int,input().split())
        if n == 1:
            results.append(a)
        else:
            if a * 2 > b:
                results.append((n//2) * b + (n % 2) * a)
            else:
                results.append(a * n)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()