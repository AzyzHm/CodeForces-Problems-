def solver(n,a):
    a.sort()
    diff = []
    for i in range(n-1):
        diff.append(abs(a[i]-a[i+1]))
    return min(diff)
def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        result.append(solver(n,a))
    for i in result:
        print(i)
        

if __name__ == '__main__':
    main()