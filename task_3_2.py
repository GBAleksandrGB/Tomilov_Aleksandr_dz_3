def num_translate_adv(word=input('Введите слово от 0 до 10 ')):
    if word.istitle():
        try:
            print(words.get(word.lower()).capitalize())
        # capitalize() и NoneType даст ошибку, например если ввести Yen вместо Ten
        except AttributeError:
            print(None)
    else:
        print(words.get(word))


words = {'null': 'ноль', 'one': 'один',
         'two': 'два', 'three': 'три',
         'four': 'четыре', 'five': 'пять',
         'six': 'шесть', 'seven': 'семь',
         'eight': 'восемь', 'nine': 'девять',
         'ten': 'десять'}

num_translate_adv()
