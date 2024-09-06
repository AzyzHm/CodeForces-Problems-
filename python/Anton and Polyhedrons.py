def main():
    polyhedrons = {
        'Tetrahedron' : 4,
        'Cube' : 6,
        'Octahedron' : 8,
        'Dodecahedron' : 12,
        'Icosahedron' : 20
    }
    n = int(input())
    sum = 0
    for _ in range(n):
        polyhedron = input()
        sum += polyhedrons[polyhedron]
    print(sum)

if __name__ == "__main__":
    main()