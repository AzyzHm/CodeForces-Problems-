def main():
    s = input()
    t = input()
    index = 0
    for i in range(len(t)):
        if t[i] == s[index]:
            index += 1
    index += 1
    print(index)
if __name__ == '__main__':
    main()