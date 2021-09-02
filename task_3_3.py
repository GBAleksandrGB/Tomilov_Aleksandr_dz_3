def thesaurus(*args):
    keys_list = []

    for name in args:
        key = name[0]
        if key not in keys_list:
            keys_list.append(key)

    val_list = []
    for key in keys_list:
        val = list(filter(lambda el: el[0] == key, args))
        val_list.append(val)

    names = zip(keys_list, val_list)
    names = (dict(names))  # распаковка ** не срабатывается для zip
    print(names)
    sorted_names = dict(sorted(names.items(), key=lambda x: x[0]))
    print(sorted_names)


thesaurus("Иван", "Мария", "Петр", "Илья", "Абракадабра")
