def main():
    t = int(input())
    results = []
    for _ in range(t):
        notes = []
        n = int(input())
        for i in range(n):
            s = input()
            notes.insert(0,s.index('#')+1)
        results.append(notes)
    for result in results:
        print(*result)

if __name__ == '__main__':
    main()