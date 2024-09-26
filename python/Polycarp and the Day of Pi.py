def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = input()
        pi = '314159265358979323846264338327'
        count = 0
        for i in range(len(n)):
            if n[i] == pi[i]:
                count += 1
            else:
                break
        results.append(count)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()