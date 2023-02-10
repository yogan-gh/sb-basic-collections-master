def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    old_video_cards = []
    count_video_card = int(input("Количество видеокарт: "))
    for i in range(1, count_video_card + 1):
        print(f"{i} Видеокарта:", end=" ")
        video_card = int(input())
        old_video_cards.append(video_card)
    return old_video_cards

def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print(f"Старый список видеокарт: {old_video_cards}")
    print(f"Новый список видеокарт: {new_video_cards}")


def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    new_video_card = []
    top_video_card = max(video_cards)
    for i_video_card in video_cards:
        if i_video_card != top_video_card:
            new_video_card.append(i_video_card)
    return new_video_card


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
