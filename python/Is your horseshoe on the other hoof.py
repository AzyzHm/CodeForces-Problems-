def main():
    a = list(map(int,input().split()))
    colors  = set(a)
    print(4 - len(colors))

if __name__ == "__main__":
    main()