# Игра в слова
import requests
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random}


def search_word(inp_word):
    url = f"https://ru.wikipedia.org/w/index.php?search={inp_word}&" \
          f"title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:" \
          f"%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&profile=advanced&fulltext=1&ns0=1 "
    response = requests.get(url, headers=headers)
    soup = Bs(response.text, "lxml")
    try:
        data = soup.find("ul", class_="mw-search-results")
        if len(data) != 0:
            exists_word = data.find("span", class_="searchmatch").text.lower()
            return True
    except TypeError:
        return False

name_list = []
word_list = []
res = {}
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
                while not search_word(slovo):
                    print("Такого слова не существует!")
                    slovo = input(f'{i}, введите слово: \n').lower()
                word_list.append(slovo)
                res[i] += 1
            else:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                while not search_word(slovo):
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
                        elif not search_word(slovo):
                            print("Такого слова не существует!")
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        else:
                            word_list.append(slovo)
                            res[i] += 1
                            break


player_name()
print('Игра началась! Чтобы закончить игру введите "stop".')
word()
