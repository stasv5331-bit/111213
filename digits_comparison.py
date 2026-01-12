from digits_basic import remove_leading_zeros

def compare_numbers(a: list, b: list) -> int:
    """
    Сравнивает два числа в виде массивов цифр
    Возвращает: 1 если a > b, 0 если a == b, -1 если a < b
    """
    # Удаляем ведущие нули
    num1 = remove_leading_zeros(a)
    num2 = remove_leading_zeros(b)
    
    # Сравнение по длине
    if len(num1) > len(num2):
        return 1
    if len(num1) < len(num2):
        return -1
    
    # Поразрядное сравнение
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return 1
        if num1[i] < num2[i]:
            return -1
    
    return 0  # Равны

def is_greater_or_equal(a: list, b: list) -> bool:
    """Проверяет, что a >= b"""
    return compare_numbers(a, b) >= 0