import sys
lines = []
with open("life-expectancy.csv") as list:
    for line in list:
        cleanline = line.strip()
        lines.append(cleanline.split(","))
        
del lines[0]
min = float(sys.maxsize)
for line in lines:
    if float(line[3]) < min:
        min = float(line[3])
        minname = line[0]
        minyear= line[2]

max = 0.0
for line in lines:
    if(float(line[3])> max):
        max = float(line[3])
        maxname = line[0]
        maxyear = line[2]
        

print()
print(f"The overall max life expectancy is: {max} from {maxname} in {maxyear}")
print(f"The overall min life expectancy is: {min} from {minname} in {minyear}")
years = []

ans = ""
while ans != "no":
    print()
    year = int(input("Enter the year of interest: "))
    with open("life-expectancy.csv") as list:
    
        count = 0
        for line in list:
            if count != 0:
                cleanline = line.strip()
                split = cleanline.split(",")
                if int(split[2]) == year:
                    years.append(split)
            count += 1
    
    total = 0.0
    for line in years:
        total += float(line[3])
    if len(years) > 1:
        avg = total / len(years)
    else:
        print("length is zero bozo")
        avg = "kys"
    print()
    print(f"For the year {year}:")
    print(f"The average life expectancy across all countries was {avg:.2f}")
    min = float(sys.maxsize)
    for line in years:
        if float(line[3]) < min:
            min = float(line[3])
            minname = line[0]
            minyear= line[2]

    max = 0.0
    for line in years:
        if(float(line[3])> max):
            max = float(line[3])
            maxname = line[0]
            maxyear = line[2]
    print()
    print(f"The max life expectancy was in {maxname} with {max:.2f}")
    print(f"The min life expectancy was in {minname} with {min:.2f}")
    ans = input("would you like to see another year? (type yes or no) ")

            
