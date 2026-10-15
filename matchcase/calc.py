num1 = float(input('Введите первое число: '))
symbol = input('Введите символ операции (+ - * /): ')
num2 = float(input('Введите второе число: '))

match symbol:
    case '+':
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
    case '*':
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')
    case '-':
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')
    case '/':
        if num2 == 0:
            print('ОШИБКА! Делить на ноль нельзя.')
        else:
            result = num1 / num2
            print(f'{num1} / {num2} = {result}')
    case _:
        print('ОШИБКА! Неизвестная операция.')
