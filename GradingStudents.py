def grading_students(grades):
    new_grades = []
    for i in grades:
        if (i >=38):
            c = i
            while True:
                if (c%5 != 0):
                    c += 1
                else:
                    break
            if ((c-i)<3):
                new_grades.append(c)
            else:
                new_grades.append(i)
        else:
            new_grades.append(i)
    print(new_grades)
grading_students([15,97,55,87,88,99,66])