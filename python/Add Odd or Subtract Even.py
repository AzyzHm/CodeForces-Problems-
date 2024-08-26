def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b = map(int,input().split())
        if a == b:
            results.append(0)
        elif a > b:
            if (a-b) % 2 == 1:
                results.append(2)
            else:
                results.append(1)
        else:
            if (b-a) % 2 == 0:
                results.append(2)
            else:
                results.append(1)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()