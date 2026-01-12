from digits_basic import number_to_digits, print_digits
from digits_subtraction import subtract_numbers

def test_subtraction():
    print("\n=== Тестирование вычитания ===")
    
    # Тест 1: Простое вычитание
    num1 = number_to_digits(1000)
    num2 = number_to_digits(1)
    diff_result = subtract_numbers(num1, num2)
    print("1000 - 1 = ", end="")
    print_digits(diff_result)
    
    # Тест 2: С заимствованием
    num3 = number_to_digits(1234)
    num4 = number_to_digits(567)
    diff_result2 = subtract_numbers(num3, num4)
    print("1234 - 567 = ", end="")
    print_digits(diff_result2)
    
    # Тест 3: Большие числа
    num5 = number_to_digits(987654321)
    num6 = number_to_digits(123456789)
    diff_result3 = subtract_numbers(num5, num6)
    print("987654321 - 123456789 = ", end="")
    print_digits(diff_result3)
    
    # Тест 4: Попытка вычесть большее число
    try:
        num7 = number_to_digits(100)
        num8 = number_to_digits(200)
        diff_result4 = subtract_numbers(num7, num8)
    except ValueError as e:
        print(f"Ошибка (как и ожидалось): {e}")

if __name__ == "__main__":
    test_subtraction()