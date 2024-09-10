def main():
    string = 'codeforces'
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        if s in string:
            results.append('Yes')
        else:
            results.append('No')
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()