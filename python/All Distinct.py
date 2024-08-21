def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if len(a) == len(set(a)):
            results.append(len(a))
            continue
        if len(a) % 2 == 0 and len(set(a)) % 2 == 0:
            results.append(len(set(a)))
            continue
        if len(a) % 2 == 0 and len(set(a)) % 2 != 0:
            results.append(len(set(a))-1)
            continue
        if len(a) % 2 != 0 and len(set(a)) % 2 == 0:
            results.append(len(set(a))-1)
            continue
        if len(a) % 2 != 0 and len(set(a)) % 2 != 0:
            results.append(len(set(a)))
            continue

    for i in results:
        print(i)
            

if __name__ == '__main__':
    main()