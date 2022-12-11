def breaking_records(scores):
    max_value, min_value = scores[0], scores[0]
    max_breaked, min_breaked = 0, 0

    for i in scores:
        if i > max_value:
            max_value = i
            max_breaked += 1

        elif i < min_value:
            min_value = i
            min_breaked += 1    

    print(max_breaked, min_breaked)


breaking_records([10,20,30,5,1,55])