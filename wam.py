import sys, os

# File rows
# Year, Semester, Unit, Unit_name, Mark, Grade, Credit_points

file = open(os.path.join(sys.argv[1]))
lines = file.readlines()
unit_info = []
for i in lines:
    unit_info.append(i.strip("\n").split("\t"))

def wam_engeering(unit_info):
    marks = []
    sum_credits = 0
    for i in range(len(unit_info)):
        marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
        sum_credits = sum_credits + float(unit_info[i][6])
    #print(sorted(marks, reverse=True))
    average = sum(marks) / sum_credits
    return str(round(average, 1))

def covid_wam(unit_info):
    marks = []
    sum_credits = 0
    for i in range(len(unit_info)):
        if unit_info[i][0] == "2020":
            if unit_info[i][1] != "S1C" and unit_info[i][1] != "S1CIJA":
                marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
                sum_credits = sum_credits + float(unit_info[i][6])
        else:
            marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
            sum_credits = sum_credits + float(unit_info[i][6])
    average = sum(marks) / sum_credits
    return str(round(average, 1))

def grade_count(grade):
    count = 0
    for i in range(len(unit_info)):
        if unit_info[i][5] == grade:
            count = count + 1
    return count

def AAM(unit_info):
    annual_marks = []
    annual_cp = []
    current_year = unit_info[0][0]
    for i in range(len(unit_info)):
        if unit_info[i][0] != current_year:
            aam = sum(annual_marks) / sum(annual_cp)
            print(current_year + ": " + str(round(aam,1)))
            annual_marks = []
            annual_cp = []
            current_year = unit_info[i][0]
        elif unit_info[i][0] == current_year:
            annual_marks.append(float(unit_info[i][4]) * float(unit_info[i][6]))
            annual_cp.append(float(unit_info[i][6]))
            if unit_info[-1][0] == current_year:
                aam = sum(annual_marks) / sum(annual_cp)
                print(current_year + ": " + str(round(aam,1)))
                break

            



print("")
print("Grade Overview: ")
print("HD: " + str(grade_count("HD")))
print("DI: " + str(grade_count("DI")))
print("CR: " + str(grade_count("CR")))
print("PS: " + str(grade_count("PS")))
print("FA: " + str(grade_count("FA")))
print("")
print("Weighted Average Mark (WAM): " + wam_engeering(unit_info))
print("Converted WAM (CWAM): " + covid_wam(unit_info))
print("")
print("Annual Average Mark (AAM): ")
AAM(unit_info)
print("")