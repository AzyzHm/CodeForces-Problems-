def minimum_diff(arr,avoided:list):
    diff = 99999
    for i in range(len(arr)-1):
        if i in avoided and i+1 in avoided:
            continue
        if diff > arr[i+1] - arr[i]:
            diff = arr[i+1] - arr[i]
            a = arr[i]
            b = arr[i+1]
    return diff,a,b

def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    avoidings = []
    total = 0
    for i in range(n-1):
        diff,a,b = minimum_diff(arr,avoidings)
        avoidings.append(a)
        avoidings.append(b)
        total += diff
    print(total)
        
        

if __name__ == '__main__':
    main()