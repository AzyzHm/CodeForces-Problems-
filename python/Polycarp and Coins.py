def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        x = n // 3
        y = (n - x)//2
        x += (n-x-y*2)
        results.append([x,y])

    for result in results:
        print(result[0],result[1])
        

if __name__ == "__main__":
    main()