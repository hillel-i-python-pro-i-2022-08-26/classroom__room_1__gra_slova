# Игра в слова
import requests
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random}


def rus_dict_parse():
    page_number = 1
    for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
        url = f"https://ozhegov.slovaronline.com/articles/{letter}/page-{page_number}"
        response = requests.get(url, headers=headers)
        soup = Bs(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 col-sm-12 article-link")
        if len(data) != 0:
            page_number += 1
        else:
            page_number = 1
            continue
        if len(data) != 0:
            for words in data:
                dict_word = words.find("a").text.strip(".?").lower()
                dictionary.append(dict_word)
        else:
            break


print("Начните игру после появления приветствия на экране")
name_list = []
word_list = []
res = {}
dictionary = []
rus_dict_parse()
print('Вас приветсвует игра в слова.')
print('Для начала введите имя игрока. Введите "start" для начала игры.')


def player_name():
    while True:
        name = input('Введите имя: \n')
        if name == 'start':
            break
        name_list.append(name.title())
        res.setdefault(name.title(), 0)


def word():
    while True:
        for i in name_list:
            if len(word_list) == 0:
                slovo = input(f'{i}, введите слово: \n').lower()
                while slovo not in dictionary:
                    print("Такого слова не существует!")
                    slovo = input(f'{i}, введите слово: \n').lower()
                word_list.append(slovo)
                res[i] += 1
            else:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                while slovo not in dictionary:
                    print("Такого слова не существует!")
                    slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                    if slovo == 'stop':
                        for key, value in res.items():
                            print(f'{key}, ввел {value} слов!')
                        print('***********************')
                        print(f'Всего введено слов: {len(word_list)}')
                        exit()
                if slovo == 'stop':
                    for key, value in res.items():
                        print(f'{key}, ввел {value} слов!')
                    print('***********************')
                    print(f'Всего введено слов: {len(word_list)}')
                    exit()
                else:
                    while True:
                        if slovo == 'stop':
                            for key, value in res.items():
                                print(f'{key}, ввел {value} слов!')
                            print('***********************')
                            print(f'Всего введено слов: {len(word_list)}')
                            exit()
                        elif not slovo.startswith(last_word[-1]):
                            print('Это слово начинаеться с другой буквы!')
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        elif slovo in word_list:
                            print('Это слово уже использовалось, введите другое: \n')
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        elif slovo not in dictionary:
                            print("Такого слова не существует!")
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        else:
                            word_list.append(slovo)
                            res[i] += 1
                            break


player_name()
print('Игра началась! Чтобы закончить игру введите "stop".')
word()
