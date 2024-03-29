import curses
from random import randint

def создать_поле_игры(высота, ширина):
    поле = [[' ' for _ in range(ширина)] for _ in range(высота)]
    return поле

def нарисовать_поле(окно, поле):
    окно.clear()
    высота, ширина = len(поле), len(поле[0])
    for i in range(высота):
        for j in range(ширина):
            окно.addch(i, j * 2, поле[i][j])
    окно.refresh()

def падение_фигуры(фигура, поле, текущая_позиция, цвет):
    for i in range(4):
        for j in range(4):
            if фигура[i][j] == 'X':
                поле[i + текущая_позиция[0]][j + текущая_позиция[1]] = цвет

def столкновение(фигура, поле, текущая_позиция):
    for i in range(4):
        for j in range(4):
            if фигура[i][j] == 'X' and поле[i + текущая_позиция[0]][j + текущая_позици[1]] != ' ':
                return True
    return False

def поворот_фигуры(фигура):
    return [list(reversed(row)) for row in zip(*фигура)]

def создать_фигуру():
    фигуры = [
        [['X', 'X', 'X', 'X']],
        [['X', 'X', 'X', ' '], [' ', ' ', ' ', 'X']],
        [['X', 'X', 'X', ' '], [' ', 'X', ' ', ' ']],
        [['X', 'X', 'X', ' '], ['X', ' ', ' ', ' ']],
        [['X', 'X', ' '], [' ', 'X', 'X']],
        [['X', 'X', ' '], ['X', 'X', ' ']],
        [['X', 'X'], ['X', 'X']]
    ]
    return фигуры[randint(0, len(фигуры) - 1)]

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    высота, ширина = 20, 10
    поле = создать_поле_игры(высота, ширина)
    
    текущая_фигура = создать_фигуру()
    текущая_позиция = [0, ширина // 2 - 2]
    цвет = curses.color_pair(randint(1, 7))

    while True:
        клавиша = stdscr.getch()

        # Движение влево
        if клавиша == curses.KEY_LEFT:
            новая_позиция = [текущая_позиция[0], текущая_позиция[1] - 1]
            if not столкновение(текущая_фигура, поле, новая_позиция):
                текущая_позиция = новая_позиция

        # Движение вправо
        elif клавиша == curses.KEY_RIGHT:
            новая_позиция = [текущая_позиция[0], текущая_позиция[1] + 1]
            if not столкновение(текущая_фигура, поле, новая_позиция):
                текущая_позиция = новая_позиция

        # Поворот
        elif клавиша == ord(' '):
            повернутая_фигура = поворот_фигуры(текущая_фигура)
            if not столкновение(повернутая_фигура, поле, текущая_позиция):
                текущая_фигура = повернутая_фигура

        # Падение
        elif клавиша == curses.KEY_DOWN:
            новая_позиция = [текущая_позиция[0] + 1, текущая_позиция[1]]
            if not столкновение(текущая_фигура, поле, новая_позиция):
                текущая_позиция = новая_позиция
            else:
                падение_фигуры(текущая_фигура, поле, текущая_позиция, цвет)
                текущая_фигура = создать_фигуру()
                текущая_позиция = [0, ширина // 2 - 2]
                цвет = curses.color_pair(randint(1, 7))

        # Отображение и очистка линий
        for i in range(высота):
            if ' ' not in поле[i]:
                поле.pop(i)
                поле.insert(0, [' '] * ширина)

        # Отображение текущей фигуры
        падение_фигуры(текущая_фигура, поле, текущая_позиция, цвет)

        # Отображение поля
        нарисовать_поле(stdscr, поле)

if __name__ == "__main__":
    curses.wrapper(main)
