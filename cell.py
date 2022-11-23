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
        btn.bind("<Button-1>", self.left_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        print(event)
        print(f"I am left clicked!")
