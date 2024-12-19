import random

def random_generator():
    print("Добро пожаловать в генератор случайных чисел!")
    print("Вы можете генерировать случайные числа в заданном диапазоне.")

    while True:
        try:
            start = int(input("Введите начальное число диапазона: "))
            end = int(input("Введите конечное число диапазона: "))

            if start >= end:
                print("Ошибка: начальное число должно быть меньше конечного.")
                continue

            random_number = random.randint(start, end)
            print(f"Случайное число в диапазоне от {start} до {end}: {random_number}")

        except ValueError:
            print("Ошибка: введите корректное целое число.")

        repeat = input("Хотите сгенерировать еще одно случайное число? (да/нет): ").lower()
        if repeat != 'да':
            print("Спасибо за использование генератора случайных чисел!")
            break

if __name__ == "__main__":
    random_generator()