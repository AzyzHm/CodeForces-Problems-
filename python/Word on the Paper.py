def main():
    t = int(input())
    results = []
    for _ in range(t):
        word = ""
        for __ in range(8):
            s = input()
            for char in s:
                if char != '.':
                    word += char
        results.append(word)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()