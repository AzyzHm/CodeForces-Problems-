def verify_strat(n,ar):
    if len(ar) == 1:
        return "YES"
    else:
        if len(ar) % 2 == 0:
            ar.sort(reverse = True)
            count = 0
            mx = 0
            for i in range(n):
                if ar[i] >= mx:
                    count += 1
                    mx = ar[i]
                    ar[i] = 0
            return "Yes" if count % 2 != 0 else "No"
        else:
            count = 0
            mx = 0
            for i in range(n):
                if ar[i] >= mx:
                    count += 1
                    mx = ar[i]
                    ar[i] = 0
            return "Yes" if count % 2 != 0 else "No"

def main():
    t = int(input())
    result = []
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        result.append(verify_strat(n,ar))
    
    for res in result:
        print(res)
        
if __name__ == '__main__':
    main()