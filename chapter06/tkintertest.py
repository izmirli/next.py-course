"""

"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.question_label = self.create_question_label()
        self.yes_but = self.create_yes_but()

    def create_question_label(self):
        text_label = tk.Label(self.master, anchor=tk.N)
        text_label["text"] = "Want to see a Python joke?"
        text_label.pack(side=tk.TOP)
        return text_label

    def create_img_label(self):
        if hasattr(self, 'joke_img'):
            # self.joke_img.pack_forget()
            # self.yes_but["text"] = "Show me!"
            self.master.destroy()
        else:
            joke_image = tk.PhotoImage(file='python_joke.gif')
            self.joke_img = tk.Label(self.master, image=joke_image)
            self.joke_img.image = joke_image
            self.joke_img.pack()
            self.yes_but["text"] = "Run away!"

    def create_yes_but(self):
        yes_but = tk.Button(self)
        yes_but["text"] = "Show me!"
        yes_but["command"] = self.create_img_label
        yes_but.pack(side=tk.BOTTOM)

        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")
        return yes_but


def main():
    root = tk.Tk()
    # root.geometry("500x475")
    app = Application(master=root)
    app.master.title('Tk Test App')
    app.mainloop()


if __name__ == '__main__':
    main()
