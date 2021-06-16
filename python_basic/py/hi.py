def swap_reference(list_ex:list, offset_x : int, offset_y : int):
    """[summary]

    Args:
        list_ex (list): [description]
        offset_x (int): [description]
        offset_y (int): [description]

    Returns:
        [type]: [description]
    """
    temp = list_ex[offset_x]
    list_ex[offset_x] = list_ex[offset_y]
    list_ex[offset_y] = temp
    return list_ex

ex = [1, 2, 3, 4, 5]
print(swap_reference(ex, 3, 4))