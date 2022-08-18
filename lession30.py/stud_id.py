import pandas as pd
#print("\nТаблица исходных данных о студентах:")
sid = {'Student Name': ['Yury', 'Evgeny', 'Sergey', 'Daria', 'Maria', 'Victor', 'Anna'],
    'Student Surname': ['Ivanov', 'Petrov', 'Maksimov', 'Sidorova', 'Kozlova', 'Popov', 'Alexandrova'],
    'Birthday': ['01.02.2016', '21.06.2015', '14.10.2012', '30.08.2010', '07.04.2007', '25.09.2008', '18.11.2014'],
    'ID': ['256', '384', '546', '132', '11', '78', '36']
    }
df = pd.DataFrame(data=sid)
# print(df)

