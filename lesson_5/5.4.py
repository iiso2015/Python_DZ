scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([n for i, n in enumerate(scr[1:], start=1) if n > scr[i - 1]])