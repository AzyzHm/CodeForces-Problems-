def main():
    n,k = map(int,input().split())
    if n % 2 == 0:
        if k <= n//2:
            print(2*k-1)
        else:
            print(2*(k-n//2))
    else:
        if k <= n//2 + 1:
            print(2*k-1)
        else:
            print(2*(k-n//2)-2)
if __name__ == '__main__':
    main()