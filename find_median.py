def findMedian(arr):
 arr.sort()
 middle = len(arr)//2
 return arr[middle]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(findMedian(arr))