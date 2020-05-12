from tkinter import PhotoImage

import card_images as ci


class CardFaces:
    FACES = {}
    BACK = None
    W = 72
    H = 96
    tile = None

    @staticmethod
    def _create_back():
        pict = PhotoImage(file='card_jfitz_back.png')
        CardFaces.BACK = ci.part(pict, 0, 0, CardFaces.W, CardFaces.H)

    @staticmethod
    def _create_faces():
        CardFaces.tile = PhotoImage(file='cards_jfitz.png')

    @staticmethod
    def get(card):
        if card not in CardFaces.FACES:
            CardFaces.FACES[card] = ci.card_image(CardFaces.tile, card, w=CardFaces.W, h=CardFaces.H)
        return CardFaces.FACES[card]

    @staticmethod
    def create_global_images():
        if not CardFaces.FACES:
            CardFaces._create_faces()
        if not CardFaces.BACK:
            CardFaces._create_back()

    @staticmethod
    def image(card, opened):
        if opened:
            return CardFaces.get(card)
        else:
            return CardFaces.BACK
