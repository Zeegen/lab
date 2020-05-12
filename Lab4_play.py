from Lab4_deck import *


# ****************************************************************
class _PlayColumn:
    def __init__(self, decks):
        self.deck = decks
        self.row = []
        for x in range(5):
            self._put(self.deck)
            self.deck.deal()

    def can_put(self, card):
        return not self or self.top().value - 1 == card.value

    def _put(self, card):
        self.row.append(card)

    def put(self, card):
        if self.can_put(card):
            self._put(card)
            return True
        else:
            return False

    def __len__(self):
        return len(self.row)

    def top(self):
        return self.row[-1]

    def away(self):
        self.row.pop()


# ****************************************************************
class _Stack():
    def __init__(self, deck):
        self.card = None
        self.deck = deck.ACES
        self._put(self.deck[-1])
        self.deck.pop()

    def top(self):
        return self.card

    def __len__(self):
        if self.card is None:
            return 0
        return self.card.value

    def full(self):
        return len(self) == len(Deck.RANKS)

    def can_put(self, card):
        return ((self and self.top().value + 1 == card.value) and (self.top().suit == card.suit))

    def _put(self, card):
        self.card = card

    def put(self, card):
        if self.can_put(card):
            self._put(card)
            return True
        else:
            return False


# ****************************************************************
class _PlayReserve():
    def __init__(self, decks):
        self.row = []
        self.deck = decks
        self.card = None
        for x in range(13):
            self.row.append(self.deck[-1])
            self.deck.deal()

    def __len__(self):
        return len(self.row)

    def away(self):
        self.row.pop()


# ****************************************************************
class Row(tuple):
    """
    Кортеж фіксованого розміру.
    Конструктор отримує кількість елементів та iterable.
    """

    def __new__(cls, n, it):
        it = iter(it)
        obj = super().__new__(cls, (next(it) for _ in range(n)))
        return obj


# ****************************************************************
class Play:
    NBASE = 4
    NPLAY = 7
    NRESERVE = 1

    def __init__(self):
        self._deck = Decks(1)
        self._base = None
        self._play = None
        self._reserve = None
        self._in_play = False
        self.new_play()

    def new_play(self):
        self._deck.shuffle()
        iter_aces = iter(Deck.ACES)
        self._base = Row(self.NBASE, iter(lambda: _Stack(iter_aces), None))
        self._play = Row(self.NPLAY, iter(lambda: _PlayColumn(self._deck), None))
        self._reserve = Row(self.NRESERVE, iter(lambda: _PlayReserve(self._deck), None))
        self._in_play = True

    def win(self):
        res = all(stack.full() for stack in self._base.row)
        self._in_play = not res
        return res

    @staticmethod
    def move(stack_from, stack_to):
        card = stack_from.top()
        if card is None:
            return False
        res = stack_to.put(card)
        if not res:
            return False
        stack_from.away()
        return True


object = Play()
print(object)
