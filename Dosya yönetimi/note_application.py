def calculate_Notes(line):
    line = line[:-1]
    liste = line.split(':')

    studentName = liste[0]
    notes = liste[1].split(',')

    note1 = notes[0]
    note2 = notes[1]
    note3 = notes[2]
    
    average = (int(note1)+int(note2)+int(note3))/int(3)

    if average>=90 and average<=100:
        letter = 'AA'
    elif average>=85 and average<90:
        letter = 'BA'
    elif average>=70 and average<85:
        letter = 'BB'
    elif average>=50 and average<70:
        letter = 'CC'
    else:
        letter = 'FF'
    
    return studentName+ ': ' + letter + '\n'
    


def read_Averages():
    with open('exam_notes.txt', 'r', encoding= 'utf-8') as file:
        for line in file:
            print(calculate_Notes(line))
def enter_Note():
    name = input('Student name:')
    surname = input('Student surname:')
    note1 = input('Note1 :')
    note2 = input('Note2 :')
    note3 = input('Note3 :')

    with open('exam_notes.txt', 'a', encoding= 'utf-8') as file:
        file.write(name + ' ' + surname+ ': '+ note1+ ', '+ note2+ ', ' +note3 + '\n')

def record_Notes():
    with open('exam_notes.txt', 'r', encoding= 'utf-8')as file:
        liste = []

        for i in file:
            liste.append(calculate_Notes(i))

        with open('conclusion.txt', 'w', encoding= 'utf-8')as file2:
            for i in liste:
                file2.write(i)
                


while True:
    process = input("1- Read notes\n2- Enter note\n3- Record notes\n4- Exit\n")
    if process == '1':
        read_Averages()
    elif process == '2':
        enter_Note()
    elif process == '3':
        record_Notes()
    else:
        break