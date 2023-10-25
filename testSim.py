per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
mony = float(input("Введите сумму депозита: "))
deposit = [rate*(mony / 100)for rate in per_cent.values()]
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
