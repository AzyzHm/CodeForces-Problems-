def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        if s.count('A') > s.count('B'):
            results.append('A')
        else:
            results.append('B')
    for result in results:
        print(result)

if __name__ == "__main__":
    main()