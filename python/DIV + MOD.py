def solver(l: int, r: int, a: int) -> int:
    max_at_r = r // a + r % a
    max_before_reset = max(l, (r // a) * a - 1)
    max_at_reset = max_before_reset // a + max_before_reset % a
    return max(max_at_r, max_at_reset)

def main():
    t = int(input())
    tests = []
    for i in range(t):
        l,r,a = map(int, input().split())
        tests.append([l,r,a])
    for test in tests:
        l,r,a = test
        print(solver(l,r,a))

if __name__ == "__main__":
    main()