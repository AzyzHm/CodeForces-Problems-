def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,c = map(int,input().split())
        n = abs(a - b) * 2
        if a > n or b > n or c > n:
            results.append(-1)
        else:
            d = c + n // 2
            if d > n:
                d -= n
            results.append(d)
        
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()