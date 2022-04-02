def odd_number(n):
    for num in range(1, n + 1, 2):
        yield num

odd_to_15 = odd_number(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)
