if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[i, j, k] for i in range(0, x) for j in range(0, x) for k in range(0, x) if(i + k + j) != n])

