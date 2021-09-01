import random


def get_jokes(n, tag=True):
    """Выбор случайного значения из каждого списка в зависимости от n и flag"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    rand_list = []

    while n > 0:
        rand_word_1 = random.choice(nouns)
        rand_word_2 = random.choice(adverbs)
        rand_word_3 = random.choice(adjectives)
        rand_words = f'{rand_word_1} {rand_word_2} {rand_word_3}'
        rand_list.append(rand_words)

        if tag:
            nouns = list(filter(lambda el: el != rand_word_1, nouns))
            adverbs = list(filter(lambda el: el != rand_word_2, adverbs))
            adjectives = list(filter(lambda el: el != rand_word_3, adjectives))
            if n > 5:
                print('n больше 5 использовать нельзя')
                n = 5

        n -= 1

    print(rand_list)


get_jokes(6, tag=False)
