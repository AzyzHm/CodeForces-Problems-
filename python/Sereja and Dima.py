def main():
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    Sereja = 0 
    Dima = 0
    while i < n:
        if i % 2 == 0:
            if a[-1]>a[0]:
                Sereja += a[-1]
                del(a[-1])
            else:
                Sereja += a[0]
                del(a[0])
        else:
            if a[-1]>a[0]:
                Dima += a[-1]
                del(a[-1])
            else:
                Dima += a[0]
                del(a[0])
        i += 1
    
    print(Sereja,Dima)
            

if __name__ == "__main__":
    main()