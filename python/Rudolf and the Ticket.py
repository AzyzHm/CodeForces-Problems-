def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,m,k = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        count = 0
        for coin_a in a:
            for coin_b in b:
                if coin_a + coin_b <= k:
                    count += 1
        results.append(count)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()