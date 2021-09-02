def num_translate(word=input('Введите слово от 0 до 10 ')):
    print(words.get(word))


words = {'null': 'ноль', 'one': 'один',
         'two': 'два', 'three': 'три',
         'four': 'четыре', 'five': 'пять',
         'six': 'шесть', 'seven': 'семь',
         'eight': 'восемь', 'nine': 'девять',
         'ten': 'десять'}

num_translate()
