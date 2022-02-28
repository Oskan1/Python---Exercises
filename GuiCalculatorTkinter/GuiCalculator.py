import tkinter

# create a graphical user interface calculator

# initiate tk
root = tkinter.Tk()

# configure GUI and grid
root.geometry('420x420')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

frame = tkinter.Frame(root, borderwidth=1, padx=20, pady=20)
frame.grid(row=2, column=2, sticky="nsew")

main_entry = tkinter.Entry(
    frame, relief=tkinter.RAISED, text="Calculator", borderwidth=1)
main_entry.grid(row=0, column=0, columnspan=5, sticky="ew")


def create_button(master, text, column, row, columnspan=1):
    """Creates and paints a button with default options that can be overwritten.

    Args:
        text ([str]): Button text
        column ([int]): Which column to be displayed in
        row ([int]): Which row to be displayed in
        columnspan (int, optional): How many columns the button spans. Defaults to 1.
    """
    button = tkinter.Button(
        master, text=text, relief=tkinter.RAISED, pady=15, padx=20)
    button.grid(column=column, row=row, columnspan=columnspan, sticky="nsew")


button_configs = [{"text": "C"},
                  {"text": "CE"},
                  {"text": "", "columnspan": 2},
                  {"text": "7"},
                  {"text": "8"},
                  {"text": "9"},
                  {"text": "+"},
                  {"text": "4"},
                  {"text": "5"},
                  {"text": "6"},
                  {"text": "-"},
                  {"text": "1"},
                  {"text": "2"},
                  {"text": "3"},
                  {"text": "*"},
                  {"text": "0"},
                  {"text": "=", "columnspan": 2},
                  {"text": "/"}]

max_columns = 4
current_row = 1
current_column = 1
for config in button_configs:
    # increment column by column span if config exists
    if ("columnspan" in config):
        create_button(frame, text=config["text"], column=current_column,
                      row=current_row, columnspan=config["columnspan"])
        current_column += config["columnspan"] - 1
    else:
        create_button(frame, text=config["text"],
                      column=current_column, row=current_row)

    # reset column count and increment row if max column is reached
    if (current_column >= max_columns):
        current_row += 1
        current_column = 1
    else:
        current_column += 1

root.mainloop()