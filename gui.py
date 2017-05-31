import tkinter as tk
import mwapi


##############################################################################


def search():
    try:
        APIKEY = 'a9c87f64-80e1-4fc7-bea0-094a26a9619a'
        dictionary = mwapi.DictionaryAPI(APIKEY)
        word = entry_word.get()
        print(word)
        word.strip()
        definition = dictionary.get_definition(word)
        tf_output.insert(tk.END, definition + "\n")
    except Exception:
        print("Invalid input.")
##############################################################################


root = tk.Tk()

root.title("Dictionary Search")
root.lift()
root.minsize(250, 350)

f_main = tk.Frame(root)
f_main.grid(padx=10, pady=10)

# Title
lbl_title = tk.Label(f_main, text="Dictionary Tool", font=("System", 16))
lbl_title.grid(row=0, column=0, columnspan=3, sticky="news")

# Word Entry
lbl_word = tk.Label(f_main, text="Word:")
lbl_word.grid(row=1, column=0, sticky="e")
entry_word = tk.Entry(f_main)
entry_word.grid(row=2, column=1, sticky="w")

# Search
bt_search = tk.Button(text="Search", command=search)
bt_search.grid(row=10, column=0, sticky="news")

# Output
tf_output = tk.Text(height=20, width=5, padx=10, pady=10)
tf_output.grid(row=11, column=0, columnspan=3, sticky="news")
##############################################################################
