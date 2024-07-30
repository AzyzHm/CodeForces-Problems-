def add_random(s,pred,succ):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i != pred and i != succ:
            s += i
            break
    return s

def solve(s):
    new_string = ''
    if len(s) == 1:
        new_string += s
        new_string = add_random(new_string,s,'')
    else:
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                new_string += s[i]
                new_string = add_random(new_string,s[i],s[i+1])
                new_string += s[i+1:]
                break
            else:
                new_string += s[i]
        if len(new_string) != len(s)+1:
            new_string += s[-1]
            new_string = add_random(new_string,s[-1],'')
    return new_string
        
def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        results.append(solve(s))
    for result in results:
        print(result)

if __name__ == '__main__':
    main()