def xor(a,b):
    a = int(a)
    b = int(b)
    return str(a^b)

def is_interresting(n, s, t):
    if s == t:
        return "Yes"
    elif  n == 1:
        return "No"
    else :
        pass



def main():
    q = int(input())
    elements = []
    for i in range(q):
        n = int(input())
        s = input()
        t = input()
        elements.append((n, s, t))
    
    for element in elements:
        n, s, t = element
        s = list(s)
        t = list(t)
        print(is_interresting(n, s, t))

if __name__ == "__main__":
    main()