from tkinter import Button


class Cell:
    def __init__(self, is_mine: bool = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text="TEXT"

        )
        self.cell_btn_obj = btn
