from tkinter import PhotoImage


def _rgb(arg):
    return '#{:02x}{:02x}{:02x}'.format(*arg)


def part(source: PhotoImage, left, upper, w, h) -> PhotoImage:
    dest = PhotoImage(width=w, height=h)
    for j in range(h):
        for i in range(w):
            dest.put(_rgb(source.get(left + i, upper + j)), to=(i, j))
    return dest


def card_image(tile: PhotoImage, card, w, h) -> PhotoImage:
    return part(tile, card.j * w, card.i * h, w, h)
