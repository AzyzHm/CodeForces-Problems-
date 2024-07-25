def solver(x,y):
    if y < -1:
        return "NO"
    else:
        return "YES"
def main():
    n = int(input())
    results = []
    for _ in range(n):
        x,y = map(int,input().split())
        results.append(solver(x,y))
    for result in results:
        print(result)

if __name__ == '__main__':
    main()