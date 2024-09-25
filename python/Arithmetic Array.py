def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        k = map(int,input().split())
        total = sum(k)
        if total == n:
            results.append(0)
        elif total < n:
            results.append(1)
        else:
            results.append(total - n)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()