def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        letters = ["a","b","c","d","e","f","g","h"]
        numbers = [1,2,3,4,5,6,7,8]
        for letter in letters:
            if letter == s[0]:
                continue
            results.append(letter+s[1])
        for number in numbers:
            if number == int(s[1]):
                continue
            results.append(s[0]+str(number))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()