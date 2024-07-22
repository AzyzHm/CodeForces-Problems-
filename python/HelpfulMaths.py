def main():
    s = input()
    s = s.split('+')
    s.sort()
    print('+'.join(s))


if __name__ == '__main__':
    main()