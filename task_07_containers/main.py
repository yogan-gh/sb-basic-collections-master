def input_weight(weight):
    while True:
        weight = int(input(weight))
        if weight > 200:
            print("Вес контейнера не должен превышать 200! Повторите ввод.")
        else:
            return weight


def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    pack_count = int(input("Количество контейнеров: "))
    pack_list = []
    for _ in range(pack_count):
        pack_weight = input_weight("Введите вес контейнера: ")
        pack_list.append(pack_weight)
    pack_new_weight = input_weight("Введите вес нового контейнера: ")
    return [pack_list, pack_new_weight]


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    print(f"Номер, который получит новый контейнер: {serial_number_new_container}")


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    for index, i_container in enumerate(list_container_weights):
        if new_container_weight > i_container:
            number = index + 1
            return number
    return len(list_container_weights) + 1


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
