# solution incomplete
def solver(n,arr):
    pass

def main():
    t = int(input())
    tests = []
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        tests.append((n,arr))
    for test in tests:
        print(solver(*test))

if __name__ == '__main__':
    main()