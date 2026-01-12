from array_io import generate_digit_array, manual_digit_input, string_to_digits
from digits_basic import print_digits

def test_input_generation():
    print("\n=== Тестирование ввода и генерации ===")
    
    # Тест 1: Генерация
    print("Сгенерированное число (10 цифр): ", end="")
    gen_num = generate_digit_array(10)
    print_digits(gen_num)
    
    print("Сгенерированное число (5 цифр): ", end="")
    gen_num2 = generate_digit_array(5)
    print_digits(gen_num2)
    
    # Тест 2: Преобразование строки
    try:
        digits_from_str = string_to_digits("0012345")
        print("Строка '0012345' в цифрах: ", end="")
        print_digits(digits_from_str)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Тест 3: Ручной ввод (закомментирован для автоматического тестирования)
    # print("\nТест ручного ввода:")
    # manual_num = manual_digit_input()
    # print("Вы ввели: ", end="")
    # print_digits(manual_num)

if __name__ == "__main__":
    test_input_generation()