def main():
    t = int(input())
    results = []
    for _ in range(t):
        x = input()
        digit = int(x[0])
        length = len(x)
        presses = sum(range(1, length + 1)) + (digit - 1) * 10
        results.append(presses)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()