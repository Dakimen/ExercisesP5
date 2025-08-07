students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

def calculate_moyenne(values):
    all = 0
    for value in values:
        all += value
    moyenne = all / len(values)
    return moyenne

def main():
    student_name = input("Entrez le nom de l’étudiant :  ")
    try:
        student = students[student_name]
    except KeyError:
        print(f"L'étudiant {student_name} n'existe pas dans la liste.")
        return
    values = []
    print(f"Notes de {student_name} :  ")
    for subject in student:
        print(f"{subject} : {student[subject]}")
        values.append(students[student_name][subject])
        moyenne = calculate_moyenne(values)
    print(f"Moyenne de {student_name} : {int(moyenne)}")


main()