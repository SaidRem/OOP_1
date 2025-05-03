def palindrome_calc(phrases: list):
    result = []
    for phrase in phrases:
        test = phrase.replace(' ', '')
        if test == test[::-1]:
            result.append(phrase)
    return result


if __name__ == '__main__':
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр",
               "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = palindrome_calc(phrases)
    right_res = ["нажал кабан на баклажан", "рвал дед лавр",
                 "азот калий и лактоза",
                 "а собака боса", "тонет енот", "пуст суп"]
    assert result == right_res, f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")
