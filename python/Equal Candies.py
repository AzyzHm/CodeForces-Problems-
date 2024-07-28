def solver(n, a):
    minimum_box = min(a)
    result = 0
    for i in a:
        result += i - minimum_box
    return result
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(solver(n, a))
    for result in results:
        print(result) 

if __name__ == "__main__":
    main()