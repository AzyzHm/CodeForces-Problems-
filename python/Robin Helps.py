def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        robin_gold = 0
        give_count = 0
        
        for gold in a:
            if gold >= k:
                robin_gold += gold
            elif gold == 0 and robin_gold > 0:
                robin_gold -= 1
                give_count += 1
        
        results.append(give_count)
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()