def main():
    m,n,k = map(int,input().split())
    if n >= m and k >= m:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()