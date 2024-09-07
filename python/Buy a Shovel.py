def main():
    k, r = map(int, input().split())
    for number_of_shovels in range(1, 11):
        total_price = k * number_of_shovels
        if total_price % 10 == r or total_price % 10 == 0:
            print(number_of_shovels)
            return

if __name__ == "__main__":
    main()