def element_list():
    return list(range(1, 16))


def length_of_list():
    return len(element_list())


def duplicate_of_list():
    list1 = list(range(1, 16))
    duplicate_list = []
    for i in list1:
        duplicate_list.append(i)
    return duplicate_list


def removal_of_duplicate_of_list():
    new_list = duplicate_of_list()
    opened_list = []
    for i in new_list:
        if i not in opened_list:
            opened_list.append(i)
    return opened_list


