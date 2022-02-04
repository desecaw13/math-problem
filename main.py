from time import time
from tkinter import Tk, IntVar, Label, Button, messagebox, DISABLED

# 1/300 + 1/500 = 1/t
# calculated: t = 187.5
# timed: t = ~190

def workShort():
    if count.get() > 0:
        count.set(count.get() - 1)
        buttons[count.get()].configure(bg='#10E010') # short is green
        root.after(short_time, workShort)
    else:
        end_time = time()
        print(f"short: {end_time - start_time} seconds")
        showEnd(end_time, start_time)

def workLong():
    if count.get() > 0:
        count.set(count.get() - 1)
        buttons[count.get()].configure(bg='#1010E0') # long is blue
        root.after(long_time, workLong)
    else:
        end_time = time()
        print(f"long: {end_time - start_time} seconds")
        showEnd(end_time, start_time)

def showEnd(end_time, start_time):
    global isDone
    if not isDone:
        isDone = True
        messagebox.showinfo('Time', f'Took {end_time - start_time :.2f} seconds.')


if __name__ == '__main__':
    short_time = 3000
    long_time = 5000

    root = Tk()

    count = IntVar(root, 100)

    Label(root, textvariable=count).grid(columnspan=100)

    buttons = [0]*100
    for i in range(len(buttons)):
        tmp_b = Button(root, state=DISABLED)
        tmp_b.grid(row=1, column=i)
        buttons[i] = tmp_b

    isDone = False

    start_time = time()

    root.after(short_time, workShort)
    root.after(long_time, workLong)

    root.mainloop()
