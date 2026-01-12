from digits_basic import remove_leading_zeros
from digits_comparison import compare_numbers

def subtract_numbers(a: list, b: list) -> list:
    """Вычитает b из a (a - b), где a >= b"""
    # Проверяем, что a >= b
    if compare_numbers(a, b) < 0:
        raise ValueError("Первое число должно быть больше или равно второму")
    
    result = []
    borrow = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0:
        digit_diff = a[i] - borrow
        i -= 1
        
        if j >= 0:
            digit_diff -= b[j]
            j -= 1
        
        if digit_diff < 0:
            digit_diff += 10
            borrow = 1
        else:
            borrow = 0
        
        result.insert(0, digit_diff)
    
    # Удаляем ведущие нули
    result = remove_leading_zeros(result)
    
    return result