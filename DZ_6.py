# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

distance = int(input("сколько километров пробежал в первый день? "))
goal_distance = int(input("желаемый результат: "))
n = 1

while distance < goal_distance:
    distance = distance + distance * 0.1
    n += 1

print(f"на {n}-й день спортсмен достиг результата — не менее {goal_distance} км")
