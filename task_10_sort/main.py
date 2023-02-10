def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    list_num = [1, 4, -3, 0, 10]
    print(f"Изначальный список: {list_num}")
    return list_num


def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    print(f"Отсортированный список: {sorted_list}")


def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    unsorted = True
    while unsorted:
        unsorted = False
        for index in range(len(original_list) - 1):
            if original_list[index] > original_list[index + 1]:
                unsorted = True
                original_list[index], original_list[index + 1] = original_list[index + 1], original_list[index]
    return original_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
