def main():
    n = int(input())
    coins = list(map(int, input().split()))
    sum_coins = sum(coins)
    coins.sort(reverse=True)
    sum_twin = 0
    for i in range(n):
        sum_twin += coins[i]
        if sum_twin > sum_coins - sum_twin:
            print(i+1)
            return

if __name__ == '__main__':
    main()