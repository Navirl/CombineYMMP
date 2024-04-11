import tkinter as tk
from tkinter import filedialog
import json

def select_file(entry_var):
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("YMMP Files", "*.ymmp"),))
    if file_path:
        entry_var.set(file_path)

def select_folder(entry_var):
    folder_path = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    if folder_path:
        entry_var.set(folder_path)

def run_program():
    global target1, target2, combine, filename, maxframe
    target1 = target1_entry.get()
    target2 = target2_entry.get()
    combine = combine_entry.get()
    filename = filename_entry.get()
    #frame = int(frame_entry.get())

    with open(target1, 'r', encoding="utf-8-sig") as file:
        data = json.load(file)

    with open(target2, 'r', encoding="utf-8-sig") as file:
        data2 = json.load(file)

    maxframe = max(item['Frame'] + item['Length'] for item in data['Timeline']['Items'])

    updated_items = []
    for item in data2['Timeline']['Items']:
        item['Frame'] += maxframe
        updated_items.append(item)

    data['Timeline']['Items'].extend(updated_items)

    with open(combine + '/' + filename + '.ymmp', 'w', encoding="utf-8-sig") as file:
        json.dump(data, file, indent=4)

    result_label.config(text="結合完了")

root = tk.Tk()
root.title("YMMP結合ツール")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# StringVarを使用して、選択されたファイルパスを保存
target1_entry = tk.StringVar()
target2_entry = tk.StringVar()
combine_entry = tk.StringVar()
filename_entry = tk.StringVar()

target1_label = tk.Label(frame, text="Target1:")
target1_label.grid(row=0, column=0, sticky="e")
target1_entry_widget = tk.Entry(frame, width=50, textvariable=target1_entry)
target1_entry_widget.grid(row=0, column=1)
target1_button = tk.Button(frame, text="選択", command=lambda e=target1_entry: select_file(e))
target1_button.grid(row=0, column=2)

target2_label = tk.Label(frame, text="Target2:")
target2_label.grid(row=1, column=0, sticky="e")
target2_entry_widget = tk.Entry(frame, width=50, textvariable=target2_entry)
target2_entry_widget.grid(row=1, column=1)
target2_button = tk.Button(frame, text="選択", command=lambda e=target2_entry: select_file(e))
target2_button.grid(row=1, column=2)

combine_label = tk.Label(frame, text="Combine:")
combine_label.grid(row=2, column=0, sticky="e")
combine_entry_widget = tk.Entry(frame, width=50, textvariable=combine_entry)
combine_entry_widget.grid(row=2, column=1)
combine_button = tk.Button(frame, text="選択", command=lambda e=combine_entry: select_folder(e))
combine_button.grid(row=2, column=2)

# ファイル名のエントリウィジェットとラベルの作成
filename_label = tk.Label(frame, text="Filename:")
filename_label.grid(row=3, column=0, sticky="e")
filename_entry_widget = tk.Entry(frame, width=50, textvariable=filename_entry)
filename_entry_widget.grid(row=3, column=1)
filename_ymmp = tk.Label(frame, text=".ymmp")
filename_ymmp.grid(row=3, column=2, sticky="e")

# フレーム数のエントリウィジェットとラベルの作成
# frame_label = tk.Label(frame, text="Frame:")
# frame_label.grid(row=4, column=0, sticky="e")
# frame_entry = tk.Entry(frame, width=50)
# frame_entry.grid(row=4, column=1)

# 実行ボタンの作成
run_button = tk.Button(frame, text="実行", command=run_program)
run_button.grid(row=4, column=0, columnspan=3)

# 結果表示ラベルの作成
result_label = tk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=3)

root.mainloop()
