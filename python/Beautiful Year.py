def main():
    year = int(input())
    result = ''
    for i in range(year+1,10000):
        temp = str(i)
        if temp.count(temp[0]) == 1 and temp.count(temp[1]) == 1 and temp.count(temp[2]) == 1:
            result = temp
            break
    print(result)


if __name__ == "__main__":
    main()