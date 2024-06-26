def get_max():
    grades = [9.6, 9.2, 9.7]

    maxValue = max(grades)
    minValue = min(grades)

    message = f"Max: {maxValue}, Min: {minValue}"
    return message

print(get_max())
