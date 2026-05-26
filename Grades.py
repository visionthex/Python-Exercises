grade = input("Enter a score between 0.0 and 0.9:\n")

try:
    final_grade = float(grade)
    if final_grade > 1.0:
        print('Bad score')
    elif final_grade >= 0.9:
        print('A')
    elif final_grade >= 0.8:
        print('B')
    elif final_grade >= 0.7:
        print('C')
    elif final_grade >= 0.6:
        print('D')
    elif final_grade < 0.6:
        print('F')
except:
    print('Bad score')