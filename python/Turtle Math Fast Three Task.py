def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        total_sum = sum(a)
        
        if total_sum % 3 == 0:
            results.append(0)
        elif n == 1:
            results.append(1)
        else:
            found = False
            for i in range(n):
                if (total_sum - a[i]) % 3 == 0:
                    results.append(1)
                    found = True
                    break
            if not found:
                if (sum(a) + 1)%3 == 0:
                    results.append(1)
                else:
                    results.append(2)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()