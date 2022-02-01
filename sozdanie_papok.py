import os

p_number = str(input('Введи номер проекта: '))
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

def make_folders():
    os.mkdir(p_number + '.00.00.00 Трансформатор')
    os.mkdir(p_number + '.00.00.00УЧ Упаковка')
    os.makedirs(f'{p_number}.10.00.00 Бак/{p_number}.10.10.00 Бак')
    os.makedirs(f'{p_number}.20.00.00 Активная часть/{p_number}.21.00.00 Крышка')
    os.makedirs(f'{p_number}.40.00.00 Расширитель/{p_number}.41.00.00 Расширитель')
    os.mkdir(p_number + '.60.00.00 Вторичные цепи')
    
make_folders()  
  
print(path)
print('Папки созданы')