import os

p_number = str(input('Введи номер проекта: '))
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

os.mkdir(p_number + '.00.00.00 Трансформатор')
os.mkdir(p_number + '.00.00.00УЧ Упаковка ')
os.mkdir(p_number + '.10.00.00 Бак')
os.mkdir(p_number + '.20.00.00 Активная часть')
os.mkdir(p_number + '.40.00.00 Расширитель')
os.mkdir(p_number + '.60.00.00 Вторичные цепи')
print(path)
print('Папки созданы')