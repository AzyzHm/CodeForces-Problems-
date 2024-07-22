def main():
    n = int(input())
    s = input()
    if s.count('A') > s.count('D'):
        print("Anton")
    elif s.count('A') < s.count('D'):
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    main()