def diagonal_diffrence(arr):
    diagonal1 = []
    diagonal2 = []
    # reversed_arr = arr.copy().reverse()
    c = 0
    for i in arr:
        diagonal1.append(i[c])
        diagonal2.append(i[-(c+1)])
        c += 1
    print(abs(sum(diagonal1) - sum(diagonal2)))
    # print(diagonal1,diagonal2)
diagonal_diffrence([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
