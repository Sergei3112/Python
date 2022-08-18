import stud_id
import stud_progress
import class_info

        
def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть успеваемость студента по ID \n \
    3: Посмотреть принадлежность по ID студента \n \
    4: Выход\n \
    Ваш выбор: '))
    
    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in stud_id.sid['Student Surname']:
            index = stud_id.sid['Student Surname'].index(Surn)
        print(f"\nID студента: {stud_id.sid['ID'][index]} \nИмя студента: {stud_id.sid['Student Name'][index]} \nФамилия студента: {stud_id.sid['Student Surname'][index]} \nДата рождения студента: {stud_id.sid['Birthday'][index]}") 
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        inp = input()
        if inp == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
        
    elif ch == 2:
        id = str(input("Введите ID студента для вывода успеваемости: "))
        if id in stud_progress.sap['ID']:
            index = stud_progress.sap['ID'].index(id)
        print(f"\nID студента: {stud_progress.sap['ID'][index]}  \nИмя студента: {stud_id.sid['Student Name'][index]} \nФамилия студента: {stud_id.sid['Student Surname'][index]} \nИстория: {stud_progress.sap['History'][index]} \nМатематика: {stud_progress.sap['Maths'][index]} \nФизика: {stud_progress.sap['Physics'][index]} \nХимия: {stud_progress.sap['Chemistry'][index]} \nОбщий процент успеваемости: {stud_progress.sap['Percentage'][index]}") 
        print('\nХотите выполнить другую операцию??? Y или N: ')
        inp = input()
        if inp == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
         
    elif ch == 3:
        cl = input('Введите ID студента для вывода принадлежности: ')
        if cl in class_info.scl['ID']:
            index = class_info.scl['ID'].index(cl)
            print(f"\nID студента: {class_info.scl['ID'][index]}  \nИмя студента: {stud_id.sid['Student Name'][index]} \nФамилия студента: {stud_id.sid['Student Surname'][index]} \nЯвляется учеником: {class_info.scl['Class'][index]}{class_info.scl['Section'][index]} класса \nСидит за партой №: {class_info.scl['Desk №'][index]} \nРяд №: {class_info.scl['Row'][index]} \nВариант №: {class_info.scl['Variation'][index]} \nОбщий процент успеваемости: {stud_progress.sap['Percentage'][index]}") 
            print('\nХотите выполнить другую операцию??? Y или N: ')
            inp = input()
            if inp == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('Всего наилучшего!')
    exit()
option()