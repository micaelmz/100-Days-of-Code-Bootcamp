import tkinter as tk

window = tk.Tk()
window.title('My first program in Tkinter')
window.minsize(width=500, height=600)
window.config(padx=30, pady=30)


# Button
def add_one():
    number_label.config(text=number_label['text'] + 1)


def greetings():
    greetings_label.config(text='Hello ' + input_name.get())


def spinbox_used():
    number_label.config(text=int(add_spin_box.get()))


def scale_used(value):
    number_label.config(text=int(value))


def checkbutton_used():
    print(checked_state.get())


# Essa mensagem nào é exibida, é trocada antes de o usuario ver
number_label = tk.Label(text='Hello Word', font=('Times New Roman', 24, 'bold'))
number_label.grid(column=1, row=0)


# Duas formas diferentes de mudar as caracteristicas de algo
number_label['text'] = '2'
number_label.config(text=3)


add_one_button = tk.Button(text='Plus one', command=add_one)
add_one_button.grid(column=0, row=1)

add_spin_box = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
add_spin_box.grid(column=1, row=1)

add_scale = tk.Scale(from_=0, to=100, command=scale_used)
add_scale.grid(column=2, row=1)

br = tk.Label(height=5)
br.grid(row=2)

# Label
greetings_label = tk.Label(text='Hello ', font=('Arial', 14, 'bold'), width=15)
greetings_label.grid(column=0, row=3)
# Text box
input_name = tk.Entry(width=20)
input_name.insert('end', 'nome')
input_name.grid(column=1, row=3)
# Button
greetings_button = tk.Button(text='Say hello', width=10, command=greetings)
greetings_button.grid(column=1, row=4)


br2 = tk.Label(height=5)
br2.grid(row=5)

checked_state = tk.BooleanVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.grid(column=0, row=6)


window.mainloop()
