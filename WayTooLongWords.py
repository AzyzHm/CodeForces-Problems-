def main():
    words = []
    n = int(input())
    for i in range(n):
        word = input()
        words.append(word)
    for word in words:
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)

if __name__ == "__main__":
    main()