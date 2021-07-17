import sys, os

# File rows
# Year, Semester, Unit, Unit_name, Mark, Grade, Credit_points

file = open(os.path.join(sys.argv[1]))
lines = file.readlines()
unit_info = []
for i in lines:
    unit_info.append(i.strip("\n").split("\t"))

marks = []
cwam_marks = []
for i in range(len(unit_info)):
    if unit_info[i][0] == "2020":
        if unit_info[i][1] != "S1C" and unit_info[i][1] != "S1CIJA":
            cwam_marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
    else:
        cwam_marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
)

    marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))

#print(sorted(marks, reverse=True))
average = sum(marks) / sum(marks)
cwam_average = sum(cwam_marks) / len(cwam_marks)

def grade_count(grade):
    count = 0
    for i in range(len(unit_info)):
        if unit_info[i][5] == grade:
            count = count + 1
    return count

print("Grade Overview: ")
print("HD: " + str(grade_count("HD")))
print("DI: " + str(grade_count("DI")))
print("CR: " + str(grade_count("CR")))
print("PS: " + str(grade_count("PS")))
print("FA: " + str(grade_count("FA")))
print("")
print("Weighted Average Mark (WAM)  = " + str(round(average, 2)))
print("Converted WAM (CWAM)  = " + str(round(cwam_average, 2)))
