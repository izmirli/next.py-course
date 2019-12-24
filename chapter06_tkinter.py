"""

"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.question_label = self.create_question_label()
        self.joke_img = self.create_img_label()
        self.create_yes_but()

    def create_question_label(self):
        text_label = tk.Label(self.master)
        text_label["text"] = "Want to see a Python joke?"
        text_label.pack(side=tk.TOP)
        return text_label

    def create_img_label(self):
        joke_image = tk.PhotoImage(file='python_joke.gif')
        joke_img = tk.Label(self, image=joke_image)
        joke_img.image = joke_img
        joke_img.pack()
        return joke_img

    def create_yes_but(self):
        yes_but = tk.Button(self)
        yes_but["text"] = "Show me!"
        yes_but["command"] = self.joke_img.pack()
        yes_but.pack(side="bottom")

        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.master.title('Tk Test App')
    app.mainloop()


if __name__ == '__main__':
    main()
