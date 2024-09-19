def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        b = list(map(int,input().split()))
        new_list = []
        i = 0
        while i < n:
            if i % 2 == 0:
                new_list.append(b[0])
                del(b[0])
            else:
                new_list.append(b[-1])
                del(b[-1])
            i += 1
        results.append(new_list)
    for result in results:
        print(*result)

if __name__ == '__main__':
    main()