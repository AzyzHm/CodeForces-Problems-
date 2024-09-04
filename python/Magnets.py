def main():
    n = int(input())
    num_groups = 0
    a = []
    for i in range(n):
        if i == 0:
            a.append(input())
            num_groups += 1
        else:
            a.append(input())
            if a[i] != a[i-1]:
                num_groups += 1
    print(num_groups)
    

if __name__ == "__main__":
    main()