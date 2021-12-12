import re
subj = {}
with open('f6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        lecture1 = re.sub(r'-', '0', lecture)
        practice1 = re.sub(r'-', '0', practice)
        lab1 = re.sub(r'-', '0', lab)
        lecture2 = int(re.sub(r'[а-я-()]', '', lecture1))
        practice2 = int(re.sub(r'[а-я-()]', '', practice1))
        lab2 = int(re.sub(r'[а-я-()]', '', lab1))
        subject1 = re.sub(r':', '', subject)
        subj[subject1] = (lecture2) + (practice2) + (lab2)
    print(f'Общее количество часов по предметам - \n{subj}')