def main():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    kth_score = scores[k-1]
    count = 0
    for i in range(n):
        if scores[i] >= kth_score and scores[i] > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()