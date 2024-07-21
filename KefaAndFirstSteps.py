def main():
    n = int(input())
    numbers = list(map(int,input().split()))
    max_length = 1
    length = 1
    for i in range(n-1):
        if numbers[i] <= numbers[i+1]:
            length += 1
            max_length = max(max_length,length)
        else:
            max_length = max(max_length,length)
            length = 1
    print(max_length)

if __name__ == '__main__':
    main()