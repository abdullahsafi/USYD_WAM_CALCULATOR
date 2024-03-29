import sys, os, re

# Year, Semester, Unit, Unit_name, Mark, Grade, Credit_points
file = open(os.path.join(sys.argv[1]))
lines = file.readlines()
unit_info = []
for i in lines:
    unit_info.append(i.strip("\n").split("\t"))

"""
Σ(Wi x CPi x Mi) / Σ(Wi x CPi)

Wi is the weighting given by 0 for 1000 level units of study, 2 for 2000 level units, 
3 for 3000 level units and 4 for 4000 level or above units. 

Thesis units of study are given a double weighting of 8.

CPi is the number of credit points for the unit of study.

Mi is the mark achieved for the unit of study.
"""
def EIHWAM(info):
    unit_wam_cal = []
    unit_weight_cal = []
    for course in info:
        for i, info_part in enumerate(course):
            if i == 2:
                match = re.search(r"\d", info_part)
                Wi = match.group()
                if Wi == "1":
                    Wi=0
                    continue
                if Wi == "5":
                    Wi = 4
                if Wi == "4":
                    if info_part=="INFO4911" or info_part=="INFO4912" or info_part=="INFO4913":
                        Wi = 8
                    else:
                        Wi = 4
            elif i == 4:
                Mi = info_part
            elif i == 6:
                CPi = info_part
            else:
                continue
        unit_wam_cal.append(int(Wi) * float(Mi) * int(CPi))
        unit_weight_cal.append(int(Wi) * int(CPi))
    num = sum(unit_wam_cal)
    dem = sum(unit_weight_cal)
    total = num/dem
    return total
    
    
"""
WAM=Σ (CPi x Mi) / Σ (CPi)
"""
def WAM(info):
    unit_wam_cal = []
    unit_weight_cal = []
    for course in info:
        for i, info_part in enumerate(course):
            if i == 4:
                Mi = info_part
            elif i == 6:
                CPi = info_part
            else:
                continue
        unit_wam_cal.append(int(CPi) * float(Mi))
        unit_weight_cal.append(int(CPi))
    num = sum(unit_wam_cal)
    dem = sum(unit_weight_cal)
    total = num/dem
    return total

"""
Excludes semester 1 2020
"""
def COVID_WAM(info):
    unit_wam_cal = []
    unit_weight_cal = []
    for course in info:
        covid_marked = 0
        for i, info_part in enumerate(course):
            if i==0 and info_part == "2020":
                covid_marked = 1
            elif i==1 and covid_marked == 1 and info_part == "S1C":
                CPi = 0
            else:
                covid_marked == 0
            
            if covid_marked == 0:
                # try:
                if i == 4:
                    Mi = info_part
                elif i == 6:
                    CPi = info_part
                else:
                    continue
        unit_wam_cal.append(int(CPi) * float(Mi))
        unit_weight_cal.append(int(CPi))

    num = sum(unit_wam_cal)
    dem = sum(unit_weight_cal)
    total = num/dem
    return total

"""
AAM= Per year Σ (CPi x Mi) / Σ (CPi) 
"""
def AAM(info):
    grouped_year = []

    for row in info:
        year = row[0]
        found = False

        for group in grouped_year:
            if group[0][0] == year:
                group.append(row)
                found = True
                break

        if not found:
            grouped_year.append([row])

    for year in grouped_year:
        print(year[0][0] + ": " + str(round(WAM(year),1)))
        
"""
Prints count of each grade
"""        
def grade_count(info):
    grade_counts = {"FA":0, "PS": 0, "CR": 0, "DI": 0, "HD": 0}

    for units in info:
        grade_counts[units[5]] += 1
    
    for k, v in grade_counts.items():
        print(str(k) + ": " + str(v))

print("")
print("Select a calculation using a number \"2\" or a sequence of numbers \"1 2 3\" from the following list: ")
print("")
print("1: Grade Overview")
print("2: Weighted Average Mark (WAM)")
print("3: Engineering Specific Weighted Average Mark (EIHWAM)")
print("4: Annual Average Marks (AAM)")
print("5: COVID WAM (CWAM)")

print("")
print("")

input = input("Calculation Selection: ")

try:
    input = input.split(" ")
    input = [int(x) for x in input]
    for x in input:
        if x > 5 or x < 1:
            raise Exception('Please input a correct number or sequence of numbers.')
except:
    print("")
    print("Please input a correct number or sequence of numbers.")
    exit(0)


try:
    print("")
    if 1 in input:
        print("1: Grade Overview: ")
        grade_count(unit_info)
        print("")
    if 2 in input:
        print("2: Weighted Average Mark (WAM): " + str(round(WAM(unit_info),1)))
        print("")
    if 3 in input:
        print("3: Honours EIHWAM: " + str(round(EIHWAM(unit_info),1)))
        print("")
    if 4 in input:
        print("")
        print("Annual Average Mark (AAM): ")
        AAM(unit_info)
        print("")
    if 5 in input:
        print("5: COVID WAM (CWAM): " + str(round(COVID_WAM(unit_info),1)))
        print("")
except:
    print("An error occurred with calculation. Please check format of academic_transcript.txt")