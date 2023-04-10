# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной






def reed_file():
    with open(PATH_FILE, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())


def write_file():
    with open(PATH_FILE, 'a', encoding='UTF-8') as f:
         f.writelines('\n'+input('Введите ФИО и номер человека, контакт которого нужно добавить: ')) 



def finde_file():
    find_info = input('Введите что нужно найти: ')
    with open(PATH_FILE, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)



def change_file():
    find_info = input('Введите контакт который нужно изменить: ')
    new_info = input('Введите новую информацию: ')
    with open(PATH_FILE, 'r+', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input(("Да/Нет")) == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue


PATH_FILE = r'/Users/tema/Desktop/SeminarPython/Seminar8/telefonebook.txt'

a =  int(input('Введите цифру 1, если нужно найти контакт\n Введите цифру 2, если нужно добавить контакт\n Введите цифру 3, усли хотите изменить или удалить контакт: '))
if a == 1:
    finde_file()
if a == 2:
     write_file()
if a == 3:
    change_file()

# def main():
#     write_file()

# if __name__ == '__main__':
#     main()










# def change_file():
#     find_info = input()
#     new_info = input()
#     with open(path_file,'r+',encoding='UTF-8') as f:
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 if input("Да/Нет") == "Да":
#                     lst = (line.strip()).split(' ')
#                     print(lst)
#                 else: continue
# def read_file():
#     with open(path_file,'r',encoding='UTF-8') as f:
#         for line in f:
#             print(line.strip())

# def write_file():
#     with open(path_file,'a',encoding='UTF-8') as f:
#         f.writelines('\n'+input())


# def find_file():
#     find_info = input()
#     with open(path_file,'r',encoding='UTF-8') as f:
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 print(line)


# def change_file():
#     find_info = input()
#     new_info = input()
#     with open(path_file,'r+',encoding='UTF-8') as f:
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 if input("Да/Нет") == "Да":
#                     lst = (line.strip()).split(' ')
#                     print(lst)
#                 else: continue




# def main():
#     find_file()
    


# path_file = r'Telephonebook.txt'
# if __name__ == '__main__':
#     main()