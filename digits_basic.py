def number_to_digits(number: int) -> list:
    """Преобразует число в список цифр"""
    if number == 0:
        return [0]
    
    digits = []
    while number > 0:
        digits.insert(0, number % 10)  # Вставляем в начало
        number //= 10
    return digits

def print_digits(digits: list) -> None:
    """Выводит массив цифр в читаемом формате"""
    print(f"[{', '.join(map(str, digits))}]")

def validate_digits(digits: list) -> bool:
    """Проверяет, что все элементы - цифры от 0 до 9"""
    for digit in digits:
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            return False
    return True

def remove_leading_zeros(digits: list) -> list:
    """Удаляет ведущие нули из массива цифр"""
    result = digits[:]
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result