def main():
    n = int(input())
    x = 0
    for i in range(n):
        statement = input()
        if statement.lower() == "x++" or statement.lower() == "++x":
            x += 1
        elif statement.lower() == "x--" or statement.lower() == "--x":
            x -= 1
    print(x)

if __name__ == "__main__":
    main()