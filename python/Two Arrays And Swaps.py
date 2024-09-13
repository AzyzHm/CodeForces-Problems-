def swap(a : list,b : list,k : int) -> int:
    while k > 0:
        k -= 1
        i = a.index(min(a))
        j = b.index(max(b))
        if a[i]>b[j]:
            continue
        else:
            temp = a[i]
            a[i] = b[j]
            b[j] = temp
    return sum(a)
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        results.append(swap(a,b,k))
    for result in results:
        print(result)

if __name__ == '__main__':
    main()