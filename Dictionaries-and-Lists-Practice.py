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

print (class_journal)

# Part 2: The Basic Report
# For each student, print:
# Their name
# Their list of grades
# Their average grade (rounded to 2 decimal places)


for name in class_journal:  #loop for the names of students.
  grades=0
  counter=0
  print("\n")  # to move to the next line.
  print(name,end="   ")  # printing the name and keep printing at the same line.
  print("Grades:",end=" ") # printing the grades and keep printing at the same line.
  
  for grade in class_journal[name]:  #loop to find the grades.
    print(grade,end=" ")
    grades+=grade
    counter+=1   # counter to count how many grade we have for each student.
    avg=grades/counter
    roundedAvg=round(avg,2)  #using round function to round to 2 decimal places.  (https://www.w3schools.com/python/ref_func_round.asp)
  print("Average:",roundedAvg,end=" ")








