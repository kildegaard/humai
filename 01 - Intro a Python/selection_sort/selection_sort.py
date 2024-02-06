def selection_sort(lista: list, reverse=False) -> list:
    """function that receives a unsorted list and returns a sorted one
    Args_
        lista (list): raw list, can be empty
    Returns:
        list: sorted list
    """
    sorted = []
    while lista:
        min = lista[0]
        for num in lista:
            if not reverse:
                if num < min:
                    min = num
            else:
                if num > min:
                    min = num
        sorted.append(min)
        lista.remove(min)
    return sorted


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    lista = [5, 4, 3, 2, 1]
    print(selection_sort(lista, reverse=False))
