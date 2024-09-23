def main():
    card = input()
    my_deck = [i for i in input().split()]
    found = False
    for c in my_deck:
        if card[0] == c[0] or card[1] == c[1]:
            found = True
    if found:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()