def squared_numbers(start, stop):
    squares = []
    while start <= stop:
        squares.append(start ** 2)
        start += 1
    return squares


print(squared_numbers(-3, 3))
