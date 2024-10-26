def main():
    t = int(input())
    results = []
    for _ in range(t):
        m = int(input())
        if m < 10:
            if m == 1:
                results.append(0)
            else:
                results.append(m - 1)
        else:
            power_of_10 = 1
            while power_of_10 * 10 <= m:
                power_of_10 *= 10
            results.append(m - power_of_10)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()