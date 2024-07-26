def solver(a,b,s,e):
    if s == e:
        if a[s] == b[e]:
            return 0
        else :
            return 1
    else:
        first = sorted(a[s:e+1])
        second = sorted(b[s:e+1])
        num = 0
        for i in range(len(first)):
            if second[i] not in first:
                num += 1
        if num == 0 and first != second:
            return 1
        return num
            

def main():
    t = int(input())
    results = []
    for _ in range(t):
        queries = []
        n,q = map(int, input().split())
        a = input()
        b = input()
        for _ in range(q):
            s,e = map(int, input().split())
            queries.append((s,e))
        for query in queries:
            s,e = query
            results.append(solver(a,b,s-1,e-1))
    for r in results:
        print(r)
        
    
if __name__ == '__main__':
    main()