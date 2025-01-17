def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return 1
    else:
        return 0


print(is_leap_year(2024))
