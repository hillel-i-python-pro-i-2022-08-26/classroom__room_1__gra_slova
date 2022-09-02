name_list = []
word_list = []


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
            slovo = input(f'{i}, введите слово: \n').lower()
            if len(word_list) > 0:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
                while not slovo.startswith(last_word[-1]):
                    print('Это слово начинаеться с другой буквы!')
                    slovo = input(f'{i}, введите слово на букву "{last_word[-1]}": \n').lower()
            while slovo in word_list:
                print('Это слово уже использовалось, введите другое: \n')
                slovo = input(f'{i}, введите слово: \n').lower()
            word_list.append(slovo)
            if slovo == 'exit':
                print('Спасибо за игру.')
                exit()


player_name()
word()
print(name_list, word_list)
