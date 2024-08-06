def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = input()
        results.append(int(n[0]) + int(n[1]))
    for result in results:
        print(result)

if __name__ == '__main__':
    main()