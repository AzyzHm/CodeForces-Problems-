def main():
    n,k = map(int,input().split())
    for i in range(k):
        if n%10 == 0:
            n = n//10
        else:
            n -= 1
    print(n)

if __name__ == "__main__":
    main()