class Deck:
    SUITS = ('C', 'S', 'H', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
              'K': 13}
    ALL_CARDS = ()

    class Card:
        def __init__(self, suit, rank):
            self._isuit = None
            self._irank = None
            if isinstance(suit, str) and isinstance(rank, str):
                self._init_from_str(suit, rank)
            elif isinstance(suit, int) and isinstance(rank, int):
                self._init_from_int(suit, rank)

        def _init_from_str(self, suit, rank):
            i = Deck.SUITS.index(suit)
            j = Deck.RANKS.index(rank)
            self._isuit = i
            self._irank = j

        def _init_from_int(self, suit, rank):
            if (suit < 0 or suit >= len(Deck.SUITS)) or (rank < 0 or rank >= len(Deck.RANKS)):
                raise ValueError('No such card')
            self._isuit = suit
            self._irank = rank

        def __str__(self):
            return self.suit + "-" + self.rank

        @property
        def suit(self):
            return Deck.SUITS[self._isuit]

        @property
        def rank(self):
            return Deck.RANKS[self._irank]

        @property
        def j(self):
            return self._irank

        @property
        def i(self):
            return self._isuit

        @property
        def value(self):
            return Deck.VALUES[self.rank]

        def ace(self) -> bool:
            return self.rank == 'A'

        def __hash__(self):
            return hash((self._isuit, self._irank))

        def __eq__(self, other):
            if not isinstance(other, Deck.Card):
                return NotImplemented
            return self.rank == other.rank and self.suit == other.suit

        def __lt__(self, other):
            return self.suit == other.suit and self.value < other.value


Deck.ALL_CARDS = list(Deck.Card(s, r) for s in Deck.SUITS for r in Deck.RANKS)
# tmp = list()
# for s in Deck.SUITS:
#     for r in Deck.RANKS:
#         card = Deck.Card(s, r)
#         if not card.ace():
#             tmp.append(card)
# Deck.ALL_CARDS = tmp
import random


class Decks(list):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, ndeck=1):
        self._ndeck = ndeck

    def shuffle(self):
        self.clear()
        for _ in range(self._ndeck):
            self.extend(Deck.ALL_CARDS)
        random.shuffle(self)

    def deal(self):
        return self.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        else:
            return self.deal()

    def debug(self):
        print('{ ' + '  '.join(
            (str(self[i]) + ('\n' if (i + 1) % len(Deck.RANKS) == 0 else '') for i in range(len(self)))) + ' }'
              )
