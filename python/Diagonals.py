def solver(n,k):
    if k == 0:
        return 0
    elif k <= n:
        return 1
    else:
        diagnal_size = n
        use_diagnals = 0
        while k > 0:
            if diagnal_size < n:
                for i in range(2):
                    k -= diagnal_size
                    use_diagnals += 1
                    if k <= 0:
                        return use_diagnals
                diagnal_size -= 1
            else:
                k -= diagnal_size
                use_diagnals += 1
                diagnal_size -= 1 
        return use_diagnals
def main():
    t = int(input())
    tests = []
    for i in range(t):
        n,k = map(int, input().split())
        tests.append((n,k))
    for test in tests:
        print(solver(*test))


if __name__ == '__main__':
    main()