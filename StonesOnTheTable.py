def main():
    n = int(input())
    s = input()
    number_of_stones = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            number_of_stones += 1
    print(number_of_stones)


if __name__ == '__main__':
    main()