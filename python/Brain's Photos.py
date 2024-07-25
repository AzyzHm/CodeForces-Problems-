def main():
    r,c = map(int,input().split())
    colored = False
    for i in range(r):
        colors = list(map(str,input().split()))
        if "C" in colors or "M" in colors or "Y" in colors:
            colored = True
    print("#Color") if colored else print("#Black&White")

if __name__ =='__main__':
    main()