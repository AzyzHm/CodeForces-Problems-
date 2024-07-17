def main():
    n = int(input())
    number_of_problems = 0
    for i in range(n):
        line = input().split()
        if line.count("1") >= 2:
            number_of_problems += 1
    print(number_of_problems)

if __name__ == "__main__":
    main()