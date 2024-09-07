def main():
    n = int(input())
    number_of_bills = 0
    if n >= 100:
        number_of_bills += n // 100
        n %= 100
    if n >= 20:
        number_of_bills += n // 20
        n %= 20
    if n >= 10:
        number_of_bills += n // 10
        n %= 10
    if n >= 5 :
        number_of_bills += n // 5
        n %= 5
    if n >= 1:
        number_of_bills += n // 1
        n = 0
    print(number_of_bills)

if __name__ == "__main__":
    main()