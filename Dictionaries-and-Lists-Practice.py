# part 1  Create a dictionary called class_journal, where each key is a student's name and each value is a list of all their grades.

records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

class_journal={}
for info in records:
    name=info[0]
    grade=info[1]
    if name in class_journal:
      class_journal[name].append(grade)
    else:
        class_journal[name]=[]
        class_journal[name].append(grade)

print (class_journal)

