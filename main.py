# Игра в слова
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
                word_list.append(slovo)
                res[i] += 1
            else:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
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
                        else:
                            word_list.append(slovo)
                            res[i] += 1
                            break


player_name()
print('Игра началась! Чтобы закончить игру введите "stop".')
word()
