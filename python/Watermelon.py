def main():
    weight = int(input())
    if weight % 2 == 0 and weight > 2 and weight <= 100:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()