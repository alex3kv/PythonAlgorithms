'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import namedtuple

Company = namedtuple("Company", ["name", "profit", "average"])
companies = []

count = int(input("Введите количество предприятий для расчета = "))
average_sum = 0

for i in range(count):
    print()
    name = input(f"Введите наименование организации {i+1} = ")
    company = Company(name, [], 0)

    profit_sum = 0
    for q in range(4):
        profit = float(input(f"Введите прибыль организации {i+1} за {q+1} квартал = "))
        profit_sum += profit
        company.profit.append(profit)

    company = company._replace(average = profit_sum / 4)
    companies.append(company)

    average_sum += company.average

average = average_sum / count

average_upper = [el for el in companies if el.average > average]
average_lower = [el for el in companies if el.average < average]

print()
print(f"Предприятий, чья прибыль выше среднего {average}:")
for el in average_upper:
    print(f"{el.name} ({el.average})")

print()
for el in average_lower:
    print(f"{el.name} ({el.average})")
