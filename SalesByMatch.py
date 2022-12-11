def sales_by_match(n,ar):
    p = 0
    copy_ar = ar.copy()
    for i,j in enumerate(copy_ar):
        for k, l in enumerate(copy_ar):
            if i == k and j != l:
                p += 1
    print(p)
sales_by_match(n=9,ar=[10, 20, 20, 10, 10, 30, 50, 10, 20])