from tkinter import Button


class Cell:
    def __init__(self, x: int, y: int, is_mine: bool = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind("<Button-1>", self.left_click_action)  # left click
        # btn.bind("<Button-2>", self.right_click_action)  # right click mac
        btn.bind("<Button-3>", self.right_click_action)  # right click windows
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        print(event)
        print(f"I am left clicked!")

    def right_click_action(self, event):
        print(event)
        print(f"I am right clicked!")
