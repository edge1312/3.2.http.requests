import requests

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(from_file, to_file, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(from_file, encoding='utf-8') as file:
        text = file.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(to_file, 'w', encoding='utf-8') as file:
        try:
            file.write(''.join(json_['text']))
        except KeyError:
            print(f'Язык, на который требуется перевести текст, задан неверно: {to_lang}. Попробуйте снова\n')
            define_args()
        else:
            print(f'Файл с переводом создан: {to_file}')
            print('Программа завершена')


        
def read_file_path():
    try:
        from_file = input('Введите путь(имя) к файлу с исходным текстом: ')
        file = open(from_file)
        file.close()
    except FileNotFoundError:
        print('Файл не найден. Попробуйте снова')
        from_file = read_file_path()
    else:
        print('OK\n')
    
    return from_file


def write_file_path():
    try:
        to_file = input('Задайте путь(имя) файла для сохранения результата: ') 
        file_name = to_file.split('.')
        if file_name[-1] != 'txt':
            if len(file_name) > 1:
                to_file = '.'.join(file_name) + '.txt'
            elif len(file_name) == 1:
                to_file = ''.join(file_name) + '.txt'
        file = open(to_file, 'w', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        print('Путь(имя) файла задан неверно. Попробуйте снова')
        to_file = write_file_path()
    except OSError:
        print('Путь(имя) файла задан неверно. Попробуйте снова')
        to_file = write_file_path()
    else:
        print('OK\n')

    return to_file


def define_args():
    from_file = read_file_path()
    to_file = write_file_path()
    to_lang = input('Укажите язык, на который необходимо перевести текст (по умолчанию "RU"): ')
    print()
    if to_lang == '':
        translate_it(from_file, to_file)
    else:
        translate_it(from_file, to_file, to_lang)


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':

    define_args()