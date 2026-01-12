from digits_basic import number_to_digits, print_digits
from array_io import generate_digit_array, string_to_digits
from big_number_operations import perform_operation, digits_to_string

def run_comprehensive_tests():
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ОПЕРАЦИЙ С БОЛЬШИМИ ЧИСЛАМИ")
    print("=" * 50)
    
    # Тест 1: Сложение
    print("\n1. Тест сложения:")
    num1 = number_to_digits(987654321)
    num2 = number_to_digits(123456789)
    sum_result = perform_operation(num1, num2, '+')
    print(f"   {digits_to_string(num1)} + {digits_to_string(num2)} = ", end="")
    print_digits(sum_result)
    
    # Тест 2: Вычитание
    print("\n2. Тест вычитания:")
    num3 = number_to_digits(1000000000)
    num4 = number_to_digits(999999999)
    diff_result = perform_operation(num3, num4, '-')
    print(f"   {digits_to_string(num3)} - {digits_to_string(num4)} = ", end="")
    print_digits(diff_result)
    
    # Тест 3: Генерация и операции
    print("\n3. Тест сгенерированных чисел:")
    gen1 = generate_digit_array(7)
    gen2 = generate_digit_array(7)
    
    print(f"   Число 1: ", end="")
    print_digits(gen1)
    print(f"   Число 2: ", end="")
    print_digits(gen2)
    
    gen_sum = perform_operation(gen1, gen2, '+')
    print(f"   Сумма: ", end="")
    print_digits(gen_sum)
    
    # Тест 4: Работа со строками
    print("\n4. Тест работы со строками:")
    str_num1 = "12345678901234567890"
    str_num2 = "98765432109876543210"
    
    digits1 = string_to_digits(str_num1)
    digits2 = string_to_digits(str_num2)
    
    str_sum = perform_operation(digits1, digits2, '+')
    print(f"   {str_num1} + {str_num2} = {digits_to_string(str_sum)}")
    
    # Тест 5: Обработка ошибок
    print("\n5. Тест обработки ошибок:")
    small_num = number_to_digits(100)
    large_num = number_to_digits(200)
    
    try:
        result = perform_operation(small_num, large_num, '-')
    except ValueError as e:
        print(f"   Ожидаемая ошибка: {e}")
    
    print("\n" + "=" * 50)
    print("Все тесты завершены успешно!")
    print("=" * 50)

def demonstrate_workflow():
    """Демонстрация полного рабочего процесса"""
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОЧЕГО ПРОЦЕССА")
    print("=" * 50)
    
    # Шаг 1: Ввод данных (генерация)
    print("\nШаг 1: Генерация чисел")
    num1 = generate_digit_array(5)
    num2 = generate_digit_array(5)
    print(f"Сгенерировано число 1: {digits_to_string(num1)}")
    print(f"Сгенерировано число 2: {digits_to_string(num2)}")
    
    # Шаг 2: Выполнение операции
    print("\nШаг 2: Выполнение операций")
    
    # Сложение
    sum_result = perform_operation(num1, num2, '+')
    print(f"Сложение: {digits_to_string(num1)} + {digits_to_string(num2)} = {digits_to_string(sum_result)}")
    
    # Проверяем, можно ли выполнить вычитание
    from digits_comparison import is_greater_or_equal
    if is_greater_or_equal(num1, num2):
        diff_result = perform_operation(num1, num2, '-')
        print(f"Вычитание: {digits_to_string(num1)} - {digits_to_string(num2)} = {digits_to_string(diff_result)}")
    else:
        diff_result = perform_operation(num2, num1, '-')
        print(f"Вычитание (в обратном порядке): {digits_to_string(num2)} - {digits_to_string(num1)} = {digits_to_string(diff_result)}")
    
    print("\n" + "=" * 50)
    print("Демонстрация завершена!")
    print("=" * 50)

if __name__ == "__main__":
    run_comprehensive_tests()
    demonstrate_workflow()