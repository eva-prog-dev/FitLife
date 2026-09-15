WATER_PER_KG = 30
ML_TO_LITERS = 1000


# 1. Знакомство c пользователем
print("Приветствую в приложении FitLife!")
user_name = input("Давайте познакомимся! Как Вас зовут? - ")

try:
    user_age = int(
        input(
            f"Приветствую, {user_name}, "
            "теперь введите Ваш возраст: "
        )
    )
except ValueError:
    print("Возраст должен быть целым числом")


# 2. Сбор данных
try:
    user_weight = float(
        input(
            "Теперь введите, пожалуйста, "
            "Ваш вес в килограммах: "
        )
    )
except ValueError:
    print("Введите вес числовым значением - пример: 60.5")

try:
    user_height = float(
        input("И ваш рост в метрах: ")
    )
except ValueError:
    print("Введите рост числовым значением - пример: 1.65")


# 3. Расчеты ИМТ и нормы воды в день
def bmi_calculation(weight: float, height: float):
    """Расчет ИМТ"""
    return weight / (height ** 2)


def water_calculation(weight: float):
    """Расчет необходимого количества воды в день"""
    return weight * WATER_PER_KG / ML_TO_LITERS


# 4. Вывод результата
def report():
    """Печать отчета"""
    print()
    print(
        f"Отчет для пользователя: "
        f"{user_name} ({user_age} г.)",
    )
    print(
        f"Твой Индекс Массы Тела: "
        f"{round(bmi_calculation(user_weight, user_height), 1)}",
    )
    print(
        f"Рекомендуемая норма воды: "
        f"{round(water_calculation(user_weight), 1)} л. в день",
    )
    print()
    print("Расчет окончен. Будьте здоровы!")


report()
