# part 1  Create a dictionary called class_journal, where each key is a student's name and each value is a list of all their grades.

records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

class_journal={}  #creating an empty dictinary.
for info in records:   # loop for taking the key and value.
    name=info[0]
    grade=info[1]
    if name in class_journal:
      class_journal[name].append(grade)   # adding the values.
    else:
        class_journal[name]=[]       # adding the keys wiht list data type.
        class_journal[name].append(grade)    #adding the values     .

# print (class_journal)

# Part 2: The Basic Report
# For each student, print:
# Their name
# Their list of grades
# Their average grade (rounded to 2 decimal places)

for name in class_journal:  #loop for using the names of students.
    totalGrades=0
    grades = class_journal[name]
    for i in range(len(grades)):    # searching in a list of the grades of each student to find the total grades.
      totalGrades+=grades[i]
      avg = round(totalGrades / len(grades),2)  # find the avg and rounded it to 2 decimal.
    class_journal[name] = {           # creating 2 dictionary inside each other to add the avg.
          "grades": grades,
          "average": round(avg, 2)
    }

# print(class_journal)       

#printing the names,grades and average for each student.
for name in class_journal:
  print("\nname:",name,end=", the grades: ")
  for grades in class_journal[name]["grades"]:
    print(grades,end=" ")
  print(",the average is: ",class_journal[name]["average"])

# Part 3: Deeper Analysis:

#who has the highst avg.
def highestAvg():
  highestAvg=0
  avg=0
  highestAvgName=""
  for name in class_journal:
    avg=class_journal[name]["average"]  # geting the avg of the students
    grades=class_journal[name]["grades"] # getting the grades of the students
    if avg>highestAvg:  #find the highest avg.
      highestAvg=avg
      highestAvgName=name
  print(highestAvgName,"has the highest average",highestAvg)

# Who showed the most consistent performance?
def mostConsistentPerformance():   #function to find the most consistent performance.
  dif=0
  mindif=1000
  nameStudentMin=""
  for name in class_journal:
    grades=class_journal[name]["grades"]
    highestGrade = grades[0]
    lowestGrade =  grades[0]
    
    for g in grades:            #checking the highest and lowest grade.
      if highestGrade<g:
        highestGrade=g
      if lowestGrade>g:
        lowestGrade=g
    dif=highestGrade-lowestGrade
    if dif <mindif:
        mindif=dif
        nameStudentMin=name
  print("The most consistent performance student is :",nameStudentMin)