price = [496.65, 24.56, 4.59, 49.52, 897.15, 16.65, 15, 654.61, 5, 9.69, 983.18, 61.28, 22, 7]

# пункт "А"
print('пункт "А"')
res = ''
for p in price:
    print(f'{int(p)} руб. {int(p * 100 % 100):02} коп.', end=', ')

# пункт "В"
print('\n\nпункт "В"')
print(f'список цен: {price} id списка цен:{id(price)}')

# пункт "С"
print('\nпункт"С"')
new_price = sorted(price, reverse=True)
print(f'новый список цен, отсортированных по убыванию {new_price} id нового списка цен:{id(new_price)}')

# пункт "D"
print('\nпункт "D"')
print(price[-5:])