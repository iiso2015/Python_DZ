def thesaurus(*names):
    result_names = {}
    for item in names:
        if result_names.get(item[0][0]):
            result_names[item[0][0]].append(item)
        else:
            result_names[item[0][0]] = [item]
    return (result_names)


def thesaurus_adv(*names):
    result_full_names = {}
    for item in names:
        full_name = item.split()
        full_name.reverse()
        if result_full_names.get(full_name[0][0]):
            result_full_names[full_name[0][0]].append(item)
        else:
            result_full_names[full_name[0][0]] = [item]
    for key in result_full_names:
        result_full_names[key] = thesaurus(*result_full_names[key])
    print(result_full_names)


thesaurus_adv("Пётр Иванов", "Ирина Абрамова", "Тимофей Петровский", "Ольга Серова", "Николай Филатов")