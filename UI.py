import tkinter as tk
from main import calculate_list

'''function for displaying results if user submits query'''
def display_results():
    # if query is empty, display error message
    if entry.get() == '':
        results_label["text"] = "No Query Detected"
    else:
        # if query is valid, grab results from dataset
        result = calculate_list("{}".format(entry.get()))

        # calculate longest game title in list for formatting purposes
        longest_string_len = 0
        for i in range(10):
            if len(list(result["app_name"])[i]) > longest_string_len:
                longest_string_len = len(list(result["app_name"])[i])

        # format table of results
        result_string = (("  {0:^4}     {1:^" + str(longest_string_len) + "}       {2:^10}       {3:^9}")
                         .format("rank", "title", "score", "sentiment") + (' ' * (longest_string_len // 3)) + '\n'
                         + ('_' * longest_string_len) + ('_' * 50) + (' ' * (longest_string_len // 3)))[:-4]

        for i in range(10):
            result_string += '\n'
            result_string += ("  {0:^4}  |  {1:^" + str(longest_string_len) + "}   |   {2:^10.6f}   |   {3:^9.3f}") \
                .format(i + 1, list(result["app_name"])[i], list(result["rank"])[i], list(result["avg_sentiment"])[i])
            result_string += (' ' * (longest_string_len // 3))

        # display results
        results_label["text"] = "Results:"
        results["text"] = result_string


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("2000x2000")

    # create window
    frame = tk.Frame(master=root)
    frame.pack()

    # add search bar and labels to window
    label = tk.Label(frame, text="Enter Query")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    button = tk.Button(text="generate suggestions", fg="blue", command=display_results)
    button.pack()

    results_label = tk.Label(text=0)
    results_label["text"] = ""
    results_label.pack()

    results = tk.Label(text=0, justify=tk.RIGHT, font=("Courier", 14))
    results["text"] = ""
    results.pack()

    root.mainloop()
