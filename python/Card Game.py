def main():
    t = int(input())
    results = []
    for _ in range(t):
        a1, a2, b1, b2 = map(int, input().split())
        suneet = [a1, a2]
        slavic = [b1, b2]
        number_of_games = 0
        outcomes = [
            (suneet[0], slavic[0], suneet[1], slavic[1]),
            (suneet[0], slavic[1], suneet[1], slavic[0]),
            (suneet[1], slavic[0], suneet[0], slavic[1]),
            (suneet[1], slavic[1], suneet[0], slavic[0])
        ]
        for s1, sl1, s2, sl2 in outcomes:
            suneet_wins = 0
            slavic_wins = 0
            if s1 > sl1:
                suneet_wins += 1
            elif s1 < sl1:
                slavic_wins += 1
            if s2 > sl2:
                suneet_wins += 1
            elif s2 < sl2:
                slavic_wins += 1
            if suneet_wins > slavic_wins:
                number_of_games += 1
        
        results.append(number_of_games)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
