def nb_occur(coins,coin):
    nb = 0
    for i in coins:
        if i == coin:
            nb+= 1
    return nb
def main():
    n = int(input())
    coins = list(map(int,input().split()))
    maximum_occur = 0
    for i in range(n):
        if nb_occur(coins,coins[i])>maximum_occur:
            maximum_occur = nb_occur(coins,coins[i])
    print(maximum_occur)

if __name__ == '__main__':
    main()