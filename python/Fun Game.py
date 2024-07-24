def solver(n, s, t):
    if s == t:
        return "Yes"
    elif  n == 1:
        return "No"



def main():
    q = int(input())
    elements = []
    for i in range(q):
        n = int(input())
        s = input()
        t = input()
        elements.append((n, s, t))
    
    for element in elements:
        print(solver(*element))

if __name__ == "__main__":
    main()