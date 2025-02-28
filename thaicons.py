import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "กอ ไก่ (gor gai)"),
    ("ข", "ขอ ไข่ (khor khai)"),
    ("ค", "คอ ควาย (khor khwai)"),
    ("ง", "งอ งู (ngor ngu)"),
    ("จ", "จอ จาน (jor jan)")
]


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.current_card = None

        # Flashcard UI
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, bd=3)
        self.card_frame.pack(pady=20)

        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)

        # Buttons
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.is_flipped = False

    def flip_card(self):
        if not self.is_flipped:
            self.label.config(text=self.current_card[1])
        else:
            self.label.config(text=self.current_card[0])
        self.is_flipped = not self.is_flipped


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
