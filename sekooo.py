def invest(s):
    max = 0
    second_max = 0
    profit = 0
    share = 0
    min = 0
    points = []
    for index, value in enumerate(s):
        print("index:", index, value)
        for i, v in enumerate(s):
            if (i > index):
                if (v/value > 2):
                    points.append([index, i])
    # find_best(s,points)
    assump = points[0][0]
    for j in range(len(points)):
        if assump == points[j][0]:
            share = s[points[j][1]]

            pass
        else:
            assump == points[j][0]
            share = s[points[j][1]]
    # for j in points:
    #     points[0][0]
    print(points)


# def find_best(a,x):
#     share = 0
#     dic = {}
#     for i in x:
#         now = i[0]
#         if now == i[0]:
#             # dic.update({a[0]:})
#             share = a[i[1]]
#             print(share,now)
#         # else:
#             # now =
invest([100, 50, 200, 400, 20, 60, 10, 90, 300, 200])

#[100, 50, 200, 400, 20, 60, 10, 90, 300, 200]
#[20, 30, 40, 10, 5, 80, 100, 60]
#[20, 10, 5, 30, 60, 90, 40, 50]
