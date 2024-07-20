def main():
    s = input()
    t = input()
    if s == t[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()