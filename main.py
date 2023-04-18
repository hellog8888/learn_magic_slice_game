class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

class TicTacToe:
    def __init__(self):
        self._n = 3
        self.pole = tuple(tuple(Cell() for _ in range(self._n)) for __ in range(self._n))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def correct_index(self, val):
        if type(val) != tuple or len(val) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= x < self._n) for x in val if type(x) != slice):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.correct_index(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(self._n))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(self._n))

        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.correct_index(key)
        r, c = key
        if self.pole[r][c]:
            self.pole[r][c].value = value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('клетка уже занята')
