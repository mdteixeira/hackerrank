def diagonalDifference(arr):

    princ: int = 0
    inv: int = 0

    for i in range(len(arr)):
        princ += arr[i][i]
        inv += arr[i][len(arr)-1-i]

    return abs(princ-inv)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    
    print(result)

