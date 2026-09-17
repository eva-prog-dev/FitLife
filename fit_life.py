WATER_PER_KG = 30
ML_TO_LITERS = 1000


# 1. Знакомство c пользователем
print("Приветствую в приложении FitLife!")

while True:
    user_name = input(
        "Давайте познакомимся! Как Вас зовут? - "
    ).strip()
    if not user_name:
        print("Имя не может быть пустым")
        continue

    if not user_name.isalpha():
        print("Имя должно содержать только буквы")
        continue

    break

while True:
    try:
        user_age = int(
            input(
                f"Приветствую, {user_name}, "
                "теперь введите Ваш возраст: "
            )
        )
    except ValueError:
        print("Возраст должен быть целым числом")
        continue
    if user_age <= 0:
        print("Возраст должен быть больше 0")
        continue

    break


# 2. Сбор данных
while True:
    try:
        user_weight = float(
            input(
                "Теперь введите, пожалуйста, "
                "Ваш вес в килограммах: "
            )
        )
    except ValueError:
        print("Введите вес числовым значением - пример: 60.5")
        continue
    if user_weight <= 0:
        print("Вес должен быть больше 0")
        continue

    break

while True:
    try:
        user_height = float(
            input("И ваш рост в метрах: ")
        )
    except ValueError:
        print("Введите рост числовым значением - пример: 1.65")
        continue
    if user_height <= 0:
        print("Рост должен быть больше 0")
        continue

    break


# 3. Расчеты ИМТ и нормы воды в день
def bmi_calculation(weight: float, height: float):
    """Рассчет индекса массы тела по весу и росту."""
    return weight / (height ** 2)


def water_calculation(weight: float):
    """Расчет необходимого количества воды в день."""
    return weight * WATER_PER_KG / ML_TO_LITERS


# 4. Вывод результата
def report():
    """Печать отчета."""
    print(
        "",
        f"Отчет для пользователя: "
        f"{user_name} ({user_age} г.)",
        f"Твой Индекс Массы Тела: "
        f"{round(bmi_calculation(user_weight, user_height), 1)}",
        f"Рекомендуемая норма воды: "
        f"{round(water_calculation(user_weight), 1)} л. в день",
        "",
        "Расчет окончен. Будьте здоровы!",
        sep="\n",
    )


report()
