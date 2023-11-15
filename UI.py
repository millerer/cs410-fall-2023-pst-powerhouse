import tkinter as tk


def display_results():
    print(entry.get())
    results_label["text"] = "results:"
    '''TODO make this generate a list using other code'''
    results["text"] = "Pokemon SoulSliver\n" \
                      "Legend of Zelda: Breath of the Wild\n" \
                      "Super Smash Bros: Brawl\n" \
                      "Crono Trigger\n" \
                      "Super Mario Galaxy 2\n" \
                      "Hades\n" \
                      "Ace Attorney\n" \
                      "Super Mario Bros 3\n" \
                      "Celeste\n" \
                      "Hollow Knight"


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("2000x2000")

    frame = tk.Frame(master=root)
    frame.pack()

    label = tk.Label(frame, text="Enter Title")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    button = tk.Button(text="generate suggestions", fg="blue", command=display_results)
    button.pack()

    results_label = tk.Label(text=0)
    results_label["text"] = ""
    results_label.pack()

    results = tk.Label(text=0)
    results["text"] = ""
    results.pack()

    root.mainloop()
