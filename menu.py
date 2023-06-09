from look import look, delete_contact
from print_info import print_csv, print_txt, print_all
from exceptions import user_choice
from file_writing import writing_txt, writing_scv
import get_data
from add_info import adding


def input_contact_menu_choice():
    while True:
        print()
        print('-----------------------')
        print('Управление контактами')
        print('-----------------------')
        print()
        print('1. Показать все')
        print('2. Поиск записей')
        print('3. Добавить новую запись')
        print('4. Изменить существующую запись')
        print('5. Удалить запись')
        print('6. Создать новую телефонную книгу')
        print('0. Выход')
        choice_menu = user_choice()
        if choice_menu == 1:
            print('1. вывод данных из файла Phonebook.csv в консоль')
            print('2. вывод данных из файла Phonebook.txt в консоль')
            print('3. запись данных из всех файлов в файл Phonebook_all.csv')
            print('0. Вернуться в главное меню')
            choice1 = user_choice()
            if choice1 == 1:
                print_csv()
            if choice1 == 2:
                print_txt()
            if choice1 == 3:
                print_all()
            else:
                return input_contact_menu_choice()
        elif choice_menu == 2:
            look()
        elif choice_menu == 3:
            adding()
        elif choice_menu == 4:
            return 4
        elif choice_menu == 5:
            delete_contact()
        elif choice_menu == 6:
            phonebook = get_data.data_entry()
            writing_scv(phonebook)
            writing_txt(phonebook)
            new_key = max(phonebook)
            with open('last_key.txt', "w", encoding='utf-8') as my_f:
                my_f.write(f"last_key = {new_key}")

        elif choice_menu == 0:
            return exit()
        else:
            return input_contact_menu_choice()


print(input_contact_menu_choice())
