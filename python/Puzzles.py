def solver(n:int,m:int,arr:list)->int:
    arr.sort()
    min_diff = float('inf')
    for i in range(m-n+1):
        min_diff = min(min_diff,arr[i+n-1]-arr[i])
    return min_diff

def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solver(n,m,arr))
        

if __name__ == '__main__':
    main()