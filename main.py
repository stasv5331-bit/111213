from digits_basic import number_to_digits, print_digits
from digits_comparison import compare_numbers

def test_comparison():
    print("\n=== Тестирование сравнения чисел ===")
    
    num1 = number_to_digits(12345)
    num2 = number_to_digits(12340)
    num3 = number_to_digits(999)
    
    print(f"Сравнение 12345 и 12340: {compare_numbers(num1, num2)}")
    print(f"Сравнение 12340 и 12345: {compare_numbers(num2, num1)}")
    print(f"Сравнение 12345 и 999: {compare_numbers(num1, num3)}")
    
    # Тест с ведущими нулями
    num4 = [0, 0, 1, 2, 3]
    num5 = number_to_digits(123)
    print(f"Сравнение [0,0,1,2,3] и 123: {compare_numbers(num4, num5)}")

if __name__ == "__main__":
    test_comparison()