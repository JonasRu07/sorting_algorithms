def insertion(lst: list) -> list:
    """
    insertion sort algorithm. uses side effects to modify the parameter
    :param lst: list that will get sorted
    :return: lst
    """
    for i in range(1, len(lst)):
        element = lst[i]
        for j in range(0, i-1):
            if element <= lst[j]:
                lst = [lst[j]] + lst[:j] +lst[j+1:]
                break
    return lst

def selection(lst: list) -> list:
    """
    selection sort algorithm. uses side effects to modify the parameter
    :param lst: list that will get sorted
    :return: lst
    """
    for i in range(len(lst)):
        element = lst[i]
        for j in range(i, len(lst)):
            if element > lst[j]:
                element = lst[j]
        lst.remove(element)
        lst = lst[:i] + [element] + lst[i:]
    return lst

def bubble(lst: list) -> list:
    """
    bubble sort algorithm. uses side effects to modify the parameter
    :param lst: list that will get sorted
    :return: lst
    """
    for i in range(1, len(lst)-1):
        for j in range(len(lst) - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
