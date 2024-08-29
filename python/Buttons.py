def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,c = map(int,input().split())
        if c % 2 == 0:
            if a > b:
                results.append("First")
            else:
                results.append("Second")
        else:
            if(b > a):
                results.append("Second")
            else:
                results.append("First")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()