from sys import argv

script_name, first_param, second_param, third_param = argv

four_param = int(first_param) * int(second_param) + int(third_param)

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Ваша премия: ", third_param)
print("Ваша заработная плата ", four_param)
