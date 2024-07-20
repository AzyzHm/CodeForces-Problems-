def main():
    k,n,w = map(int,input().split())
    for i in range(1,w+1):
        n -= i*k
    print(abs(min(n,0)))


if __name__ == "__main__":
    main()