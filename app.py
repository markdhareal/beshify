import customtkinter as ctk
from beshifier_folder.beshifier import BeshifierClass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        self.title("Beshify")
        self.geometry("350x450")
        self.iconbitmap("tumbling_emoji_6WJ_icon.ico")

        self.label = ctk.CTkLabel(self, text="Beshify", width=100, font=("Helvetica", 30, "bold"))
        self.label.pack(padx=10,pady=10)

        self.textBox = ctk.CTkTextbox(self, width=300, height=100, corner_radius=0)
        self.textBox.pack(padx=20,pady=20)

        self.button = ctk.CTkButton(self, text="Beshify Text", command=self.beshify_text)
        self.button.pack(padx=10,pady=10)

        self.result = ctk.CTkTextbox(self, width=300, height=100, corner_radius=0)
        self.result.pack(padx=20,pady=20)

    def beshify_text(self):
        newText = BeshifierClass.beshify(self.textBox.get("0.0","end"))
        self.textBox.delete("0.0","end")
        self.result.insert("0.0", newText)


if __name__ == "__main__":
    app = App()
    app.mainloop()