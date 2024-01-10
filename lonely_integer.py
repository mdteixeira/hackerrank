def lonelyinteger(a):
    # Write your code here
    for i in a:
        num = a.count(i)
        if num == 1:
            return i
    

array = [1, 2, 3, 4, 3, 2, 1]

print(lonelyinteger(array))