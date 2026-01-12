from digits_basic import number_to_digits, print_digits
from digits_addition import add_numbers

def test_addition():
    print("\n=== Тестирование сложения ===")
    
    # Тест 1: Простое сложение
    num1 = number_to_digits(123)
    num2 = number_to_digits(456)
    sum_result = add_numbers(num1, num2)
    print("123 + 456 = ", end="")
    print_digits(sum_result)
    
    # Тест 2: С переносом
    num3 = number_to_digits(999)
    num4 = number_to_digits(1)
    sum_result2 = add_numbers(num3, num4)
    print("999 + 1 = ", end="")
    print_digits(sum_result2)
    
    # Тест 3: Большие числа
    num5 = number_to_digits(999999999)
    num6 = number_to_digits(123456789)
    sum_result3 = add_numbers(num5, num6)
    print("999999999 + 123456789 = ", end="")
    print_digits(sum_result3)

if __name__ == "__main__":
    test_addition()