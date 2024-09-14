def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b = map(int,input().split())
        min_space = a*b * 2
        if (min(a,b)*2)**2 >= min_space:
            results.append((min(a,b)*2)**2)
        else:
            results.append(max(a,b)**2)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()