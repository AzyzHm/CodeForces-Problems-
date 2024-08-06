# not completed yet
def is_subsequence(s, t):
    it = iter(s)
    return all(c in it for c in t)

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        s = input().strip()
        t = input().strip()
        
        possible = False
        s_list = list(s)
        
        for i in range(len(s_list) - len(t) + 1):
            if all(x == "?" or x == y for x, y in zip(s_list[i:i+len(t)], t)):
                for j in range(len(t)):
                    s_list[i + j] = t[j]
                s_list = ['a' if x == '?' else x for x in s_list]
                possible = True
                break
        
        if possible and is_subsequence(s_list, t):
            results.append("YES")
            results.append("".join(s_list))
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
