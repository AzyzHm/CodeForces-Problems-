def main():
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n - 1,-1,-1):
        if a [i] == min(a):
            min_index = i
            break
    temp = a[min_index]
    del[a[min_index]]
    a.insert(n-1,temp)
    for i in range(n):
        if a[i] == max(a):
            max_index = i
            break
    print(n -1 - min_index + max_index)

if __name__ == "__main__":
    main()