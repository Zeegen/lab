def gui_demo():
    from tkinter import Tk
    from gui import GUI
    root = Tk()
    GUI(root)
    root.mainloop()


try:
    gui_demo()
except:
    pass
