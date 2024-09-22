def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,n = map(int,input().split())
        num_op = 0
        while a <= n and b <= n:
            num_op += 1
            if a < b:
                a += b
            else:
                b += a
        results.append(num_op)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()