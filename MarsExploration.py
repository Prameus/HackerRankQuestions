def mars_exploration(s):
    changes = 0
    sos = ['s','o','s']
    count = 0

    for i in s.lower():
        if i != sos[count]:
            changes += 1
        count += 1
        if count == 3:
            count = 0
        print(count,changes)
    print('result: ',changes)
mars_exploration("SOSSPSSQSSOR")
