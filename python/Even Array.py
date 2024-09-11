def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        misplaced_even = 0
        misplaced_odd = 0
        
        for i in range(n):
            if i % 2 == 0 and a[i] % 2 != 0:
                misplaced_even += 1
            elif i % 2 != 0 and a[i] % 2 == 0:
                misplaced_odd += 1
        
        if misplaced_even == misplaced_odd:
            results.append(misplaced_even)
        else:
            results.append(-1)
    for result in results:
        print(result)
if __name__ == "__main__":
    main()