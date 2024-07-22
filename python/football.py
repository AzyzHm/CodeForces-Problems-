def main():
    string = input()
    number_of_zeros = string.count('0')
    number_of_ones = string.count('1')
    if number_of_zeros >= 7:
        for i in range(len(string)):
            if string[i:i+7] == '0000000':
                print('YES')
                return
    if number_of_ones >= 7:
        for i in range(len(string)):
            if string[i:i+7] == '1111111':
                print('YES')
                return
    print('NO')
if __name__ == '__main__':
    main()