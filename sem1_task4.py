revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if revenue > costs:
    profit = revenue - costs
    print(f"Финансовый результат - прибыль ({profit})")
    print(f"Рентабельность выручки = {profit / revenue}")
    employees = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы на одного сотрудника = {profit / employees}")
elif revenue == costs:
    print("Выручка равна издержкам.")
else:
    print(f"Финансовый результат - убыток ({revenue - costs})")
