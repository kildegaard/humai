def bubble_sort(lista: list, reverse=False) -> list:
    """function that receives a unsorted list and returns a sorted one
    Args_
        lista (list): raw list, can be empty
    Returns:
        list: sorted list
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lista) - 1):
            if not reverse:
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    sorted = False
            else:
                if lista[i] < lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    sorted = False
    return lista
