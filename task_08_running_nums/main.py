def get_input_parameters():
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    list_elements = [1, 2, 3, 4, 5]
    shift = 1

    print(f"Сдвиг: {shift}")
    print(f"Изначальный список: {list_elements}")
    return [shift, list_elements]


def display_result(shifted_list):
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    print(f"Сдвинутый список: {shifted_list}")


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    list_new_elements = original_list[-shift:] + original_list[:-shift]
    return list_new_elements


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
