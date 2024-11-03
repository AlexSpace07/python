# TODO Напишите функцию find_common_participants
def find_common_participants(people1, people2, splitting_symbol='|'):
    both_participants = list(set(people1.split(splitting_symbol)).intersection(people2.split(splitting_symbol)))
    both_participants.sort()
    return both_participants

# Состав двух групп


first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

# Возврат списка общих участников

print("Общие участники встречи:", find_common_participants(first_group, second_group))
