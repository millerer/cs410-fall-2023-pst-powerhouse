import tkinter as tk
from main import calculate_list


def display_results():
    if entry.get() == '':
        results_label["text"] = "No Query Detected"
    else:
        results_label["text"] = "Calculating Results:"
        result = calculate_list(entry.get())
        print(result)
        result_list = list(result["app_name"])
        result_string = ''
        for item in result_list:
            result_string += item
            result_string += '\n'
        results_label["text"] = "Results:"
        results["text"] = result_string


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
