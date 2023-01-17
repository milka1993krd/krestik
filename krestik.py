field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
field = [['-']*3 for _ in range(3)]
def show_field(f):
    print("0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])
show_field(field)

def users_input(f):
    while True:
        place = input('введите координаты : ').split()
        if len(place)!=2:
            print('введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('введите числа')
            continue
        x, y = map(int, place)
        if not (x>=0 and x<3 and y>=0 and y<3):
            print('введите числа от 0 до 2')
            continue
        if f[x][y] != '-':
            print('клетка занята')
            continue
        break
    return x, y
users_input(field)

def win(f, user):
    win_cord = (((0, 0), (0, 1), (1, 0)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

field = [['-']*3 for _ in range(3)]
count = 0
while True:
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'
    show_field(field)
    x, y = users_input(field)
    field[x][y] = user
    if count == 9:
        print('ничья')
        break
    if win(field, user):
        print(f"выиграл {user}")
        show_field(field)
        break
    count += 1
