month = int(input('Введите номер месяца (от 1 до 12): '))

match month:
    case 1 | 2 | 12:
        print(f'{month} месяц это зима! ❄️')
    case 3 | 4 | 5:
        print(f'{month} месяц это весна! 🌸')
    case 6 | 7 | 8:
        print(f'{month} месяц это лето! ☀️')
    case 9 | 10 | 11:
        print(f'{month} месяц это осень! 🍂')
    case _:
        print('ОШИБКА! Это не номер месяца. ❌')
