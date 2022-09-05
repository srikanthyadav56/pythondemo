import tkinter

window=tkinter.Tk()
window.title("Gui")


def on_click_do_this_Task():
    tkinter.Label(window,text="Tkinter is easy to create Gui!").pack()

tkinter.button(window,text="hello",command=on_click_do_this_Task).pack()
tkinter.button(window,text="text",command=on_click_do_this_Task).pack()

window.mainloop()
