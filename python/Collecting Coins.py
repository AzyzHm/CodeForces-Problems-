def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,c,n = map(int,input().split())
        gap = (max(a,b,c) - a) + (max(a,b,c) - b) + (max(a,b,c) - c)
        n -= gap
        if n == 0:
            results.append("YES")
        else:
            if n > 0 and n % 3 == 0:
                results.append("YES")
            else:
                results.append("NO")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()