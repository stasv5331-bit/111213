from digits_basic import remove_leading_zeros

def add_numbers(a: list, b: list) -> list:
    """Складывает два числа в виде массивов цифр"""
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry > 0:
        digit_sum = carry
        
        if i >= 0:
            digit_sum += a[i]
            i -= 1
        if j >= 0:
            digit_sum += b[j]
            j -= 1
        
        result.insert(0, digit_sum % 10)
        carry = digit_sum // 10
    
    # Удаляем ведущие нули
    result = remove_leading_zeros(result)
    
    return result