def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    p = p [1:]
    q = q [1:]
    test = True
    for i in range(1,n+1):
        if i in p or i in q:
            continue
        else:
            test = False
            break
    if test:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
        
if __name__ == "__main__":
    main()