def solve(n,a):
    a.sort()
    tester = a[0]
    for i in range(1,n):
        if a[i] > tester:
            tester = a[i]
        else:
            return "No"
    return "Yes"
        
def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        result.append(solve(n,a))
    for i in result:
        print(i)

if __name__ == "__main__":
    main()