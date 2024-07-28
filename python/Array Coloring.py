def solve(a):
    return "Yes" if sum(a) % 2 == 0 else "No"
def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        result.append(solve(a))
    for i in result:
        print(i)

if __name__ == "__main__":
    main()