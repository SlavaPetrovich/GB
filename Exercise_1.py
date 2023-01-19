import random

n = int(input('Введите количество конфет: '))

while n != 0:
    print(f'осталось {n} конфет')
    a1 = int(input('Ходит первый игрок: '))
    n = n - a1
    if n <= 0:
        print('победил первый игрок')
        break
    print(f'осталось {n} конфет')
    a2 = random.randrange(1, 28)
    print(f'Ходит второй игрок: {a2}')
    n = n - a2
    if n <= 0:
        print('победил второй игрок')
        break
print('end')

