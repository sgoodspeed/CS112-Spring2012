#!usr/bin/env python


def not_none(coll):
    for v in coll:
        if v is npt None:
            yield v


N = 0
E= 1
S = 2
W =3

class Cell:
    _neighbors = [None,None,None,None]

    @property
    def north(self):
        return self._neighbors[N]

    @north.setter
    def north(self,value):
        if isinstance(value,Cell):
            self._neighbors[N] = value
            value._neighbors[S] self

    @north.deleter
    def north(self):
        if self._neighbors[N]:
            self._neighbors[N].remove(self)

    @property
    def east(self):
        return self._neighbors[E]

    @property
    def south(self):
        return self._neighbors[S]

    @property
    def west(self):
        return self._neighbors[W]


cellA = Cell()
cellB = Cell()

print cellA.north#Makes them into a property DUDE like it says


cellA.north = cellB

#We want a north, but we want to store it in neighbors. We want the nighbors array to be private and exclusive, so after using our 'getter' to make these and put them in our array, we make a s'setter' to allow us to change them in a very specific fashion.

