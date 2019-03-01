numbers = [2018, 1, 5, 0, -10, 20, 15, -7]

sorted_numbers = []
sorting = True

while sorting:
    min_numb = min(numbers)

    sorted_numbers.append(min_numb)
    numbers.remove(min_numb)

    if len(numbers) == 0:
        sorting = False


print(*sorted_numbers)
