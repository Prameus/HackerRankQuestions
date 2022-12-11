def counting_valleys(number,steps):
    hills = 0
    c1 = 0
    for i in steps:
        if (i == "U"):
            c1 += 1
            hills += is_hills(c1)
        elif (i == "D"):
            c1 -= 1
            is_hills(c1)
            hills += is_hills(c1)
            
        print(i,c1,hills)

def is_hills(hills):
    if hills == 0:
        return 1
    else:
        return 0

counting_valleys(8,"UDDDUDUU")