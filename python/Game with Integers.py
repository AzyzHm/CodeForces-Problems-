def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        if ((n+1) % 3 == 0 or (n-1) % 3 == 0):
            results.append('First')
        else:
            results.append('Second')
    for result in results:
        print(result) 

if __name__ == "__main__":
    main()