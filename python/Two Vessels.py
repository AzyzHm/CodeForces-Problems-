from math import ceil
def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,c = map(int,input().split())
        if a == b :
            results.append(0)
        else:
            amount_needed = abs(a - b) / 2
            if c > amount_needed:
                results.append(1)
            else:
                results.append(ceil(amount_needed/c))
    for result in results:
        print(result)


if __name__ == "__main__":
    main()