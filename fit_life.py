# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_TO_LITERS = 1000


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
print("Приветствую в приложении FitLife!")
user_name = input("Давайте познакомимся! Как Вас зовут? - ")

try:
    user_age = int(input(f"Приветствую , {user_name}, теперь введите Ваш возраст: "))
except ValueError:
    print("Возраст должен быть целым числом")

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
try:
    user_weight = float(input("Теперь введите, пожалуйста, Ваш вес в килограммах: "))
except ValueError:
    print("Введите вес числовым значением - пример: 60.5")

try:
    user_height = float(input("И ваш рост в метрах: "))
except ValueError:
    print("Введите вес числовым значением - пример: 1.65")


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def bmi_calculation(weight: float, height: float):
    bmi = weight / (height ** 2)

    return bmi

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_calculation(weight: float):
    water_ml = weight * WATER_PER_KG
    water_liters = water_ml / ML_TO_LITERS
    return water_liters

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
def report():
    print()
    print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
    print(f"Твой Индекс Массы Тела: {round(bmi_calculation(user_weight, user_height), 1)}")
    print(f"Рекомендуемая норма воды: {round(water_calculation(user_weight), 1)} л. в день")
    print()
    print("Расчет окончен. Будьте здоровы!")

report()
