import numpy as np


def game_core(number: int = 1, max_n=1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток 
    """
    
    count = 0  # Количество попыток
    # Половина от максимума загадываемого числа
    n = max_n // 2
    # Наше число. Сначала берем половину от максимума загадываемого числа
    predict = n

    # Реализируем цикл для проверки числа
    while number != predict:
        # + к попытке
        count += 1
        # Делим n на 2 и добавляем или убавляем от нашего числа (predict)
        n = n // 2
        # Если n обнулился добавляем к нему 1
        if n == 0: n += 1 
        # Проверка загаданного числа 
        if number > predict:
            # Если число больше добавляем n
            predict += n
        else :
            # Иначе убавляем
            predict -= n
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    max_n = 101
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, max_n, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, max_n))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


score_game(game_core)
