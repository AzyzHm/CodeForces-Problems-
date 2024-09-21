def main():
    t = int(input())
    results = []
    for _ in range(t):
        x = int(input())
        a = 1
        b = x - 1
        results.append([a,b])
    for result in results:
        print(result[0],result[1])

if __name__ == '__main__':
    main()