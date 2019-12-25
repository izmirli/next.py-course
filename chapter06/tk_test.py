import tkinter as tk

root = tk.Tk()
root.title('Tk test')

f = tk.Frame(root)
f.pack()

text_label = tk.Label(f)
text_label["text"] = "Want to see a Python joke?"
text_label.pack()

yes_but = tk.Button(f)
yes_but["text"] = "Show me!"
yes_but.pack()


def create_img_label():
    if yes_but["text"] == "Run away!":
        root.destroy()
        return

    joke_image = tk.PhotoImage(file='python_joke.gif')
    joke_img = tk.Label(root, image=joke_image)
    joke_img.image = joke_image
    joke_img.pack()
    yes_but["text"] = "Run away!"


yes_but["command"] = create_img_label


root.mainloop()
