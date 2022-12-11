def lonely_integer(ar):
    unique_ar = ar.copy()
    print(unique_ar)
    for count1,i in enumerate(ar):
        for count2, j in enumerate(ar):
            if count1 != count2:
                if i == j:
                    print(i,j)
                    unique_ar.remove(i)
    print(unique_ar)
lonely_integer([1,2,3,4,3,2,1])