# Игра в слова
name_list = []
word_list = []
print('Вас приветсвует игра в слова.')
print('Для начала введите имя игрока. Введите "start" для начала игры.')


def player_name():
    while True:
        name = input('Введите имя: \n')
        if name == 'start':
            break
        else:
            name_list.append(name)


def word():
    while True:
        for i in name_list:
            if len(word_list) == 0:
                slovo = input(f'{i}, введите слово: \n').lower()
                word_list.append(slovo)
            else:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                if slovo == 'stop':
                    exit()
                else:
                    while True:
                        if slovo == 'stop':
                            exit()
                        elif not slovo.startswith(last_word[-1]):
                            print('Это слово начинаеться с другой буквы!')
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        elif slovo in word_list:
                            print('Это слово уже использовалось, введите другое: \n')
                            slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                        else:
                            word_list.append(slovo)
                            break


player_name()
print('Игра началась! Чтобы закончить игру введите "stop".')
word()
print(name_list, word_list)
