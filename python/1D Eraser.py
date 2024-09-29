def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,k = map(int,input().split())
        s = input()
        num_op = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                num_op += 1
                i += k
            else:
                i += 1
        results.append(num_op)
    for result in results:
        print(result)
            

if __name__ == '__main__':
    main()