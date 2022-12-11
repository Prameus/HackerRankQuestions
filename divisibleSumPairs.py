def divisible_sum_pairs(n, k, ar):
    c = 0
    for count1,i in enumerate(ar):
        # print("Korega straight array da", count1, i)
        for count2, j in enumerate(ar):
            # print("Korega reverse array da",count2,j)
            if count1 != count2:
                if ((i + j) % k ) == 0:
                    c += 1
    return (int(c/2))
    
divisible_sum_pairs(6,3,[1, 3, 2, 6, 1, 2])