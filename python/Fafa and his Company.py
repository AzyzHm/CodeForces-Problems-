def main():
    n = int(input())
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()