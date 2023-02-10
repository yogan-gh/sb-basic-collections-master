def get_input_parameters():
    """
    Получаем входное слово

    :return: например: abccba
    :rtype: str
    """
    word = input("Введите слово: ")
    return word


def display_result(is_palindrome):
    """
    Выводим информацию является ли строка палиндромом

    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    if is_palindrome:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.

    :param word: слово, например: abccba
    :type word: str

    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    word_list = list(word)
    count_check = len(word) // 2
    flag_pal = True
    for index in range(1, count_check + 1):
        a = word_list[:1]
        b = word_list[-1:]
        if word_list[:1] != word_list[-1:]:
            flag_pal = False
            break
    return flag_pal


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
