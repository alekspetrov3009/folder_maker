import os

p_number = str(input('Введи номер проекта: '))
p_name = str(input('Введи название проекта: '))
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

def make_dir():
    os.mkdir(f'{p_number} {p_name}')
    os.path.abspath(path)
    
make_dir()
   
os.chdir(f'{p_number} {p_name}')

def make_folders():
    os.mkdir('!Проект')
    os.mkdir('!Стандартные и покупные изделия')
    os.mkdir(p_number + '.00.00.00 Трансформатор')
    os.mkdir(p_number + '.00.00.00УЧ Упаковка')
    os.makedirs(f'{p_number}.10.00.00 Бак/{p_number}.10.10.00 Бак')
    os.makedirs(f'{p_number}.20.00.00 Активная часть/{p_number}.21.00.00 Крышка')
    os.makedirs(f'{p_number}.40.00.00 Расширитель/{p_number}.41.00.00 Расширитель')
    os.mkdir(p_number + '.50.00.00 Система охлаждения')
    os.mkdir(p_number + '.60.00.00 Вторичные цепи')
    
make_folders() 
#make_folders()
    
print(path)
print('Папки созданы')