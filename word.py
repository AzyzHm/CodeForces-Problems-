def main():
    s = input()
    uppercases = 0
    lowercases = 0
    for letter in s:
        if letter.isupper():
            uppercases += 1
        else:
            lowercases += 1
    if uppercases > lowercases:
        print(s.upper())
    else:
        print(s.lower())


if __name__ == "__main__":
    main()