def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        c = input()
        results.append(deletions_of_two_adjacent_letters(s, c))
    for result in results:
        print(result)

def deletions_of_two_adjacent_letters(s, c):
    for i in range(len(s)):
        if s[i] == c and (i % 2 == 0):
            return "YES"
    return "NO"


if __name__ == '__main__':
    main()