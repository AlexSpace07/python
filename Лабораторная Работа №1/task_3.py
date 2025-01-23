# список игроков
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

# разделение игроков на команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# вывод сформированных команд
print("Игроки разбились на команды. Оглашаем список")
print("Первая команда:", first_team)
print("Вторая команда:", second_team)
