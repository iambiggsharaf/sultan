# array is sorted by the sum of the marks

students = [
    ["Ben", [70]], # 70
    ["Jim", [70, 50]], # 60
    ["Albert", [70, 50, 22]], #47
    ["Yakunin", [70, 50, 22, 90]], # 58
]


def averageOfList(lst):
    return sum(lst) / len(lst)

def find_student(students, average_mark):
    found = False
    student = ""
    for i in students:
        if averageOfList(i[1]) == average_mark:
            found = True
            student = i[0]
            break

    if found == True:
        return student

    else:
        maxx = -1
        for i in range(0, len(students)):
            if averageOfList(students[i][1]) > maxx and averageOfList(students[i][1]) < average_mark:
                maxx = averageOfList(students[i][1])
        
        for i in students:
            if averageOfList(i[1]) == maxx:
                return i[0]

print(find_student(students, 59))



