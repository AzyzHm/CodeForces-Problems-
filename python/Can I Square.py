from math import sqrt

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if sqrt(sum(a)) % 1 == 0:
            results.append("Yes")
        else:
            results.append("No")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()