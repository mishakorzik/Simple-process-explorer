import os, subprocess, base64
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from io import BytesIO

image = base64.b64decode('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')

root = tk.Tk()
photo = tkinter.PhotoImage(data=image)
root.wm_iconphoto(False, photo)
root.title("he1zen | file manager")
root.geometry("700x450")

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def format_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d   %H:%M:%S')

def load_directory(path):
    try:
        # Clear the treeview
        for item in tree.get_children():
            tree.delete(item)

        directories = []
        archives = []
        images = []
        files = []

        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            modification_time = os.path.getmtime(item_path)
            if os.path.isdir(item_path):
                directories.append((item, item_path, modification_time))
            else:
                size = os.path.getsize(item_path)
                do_next = True
                for check in [".zip", ".7z", ".rar", ".tar", ".tar.gz", ".tar.xz", ".bz2", ".gz", ".tbz2", ".tgz"]:
                    if do_next == True and check in str(item_path[-6:]):
                        archives.append((item, item_path, size, modification_time))
                        do_next = False
                        break
                for check in [".png", ".jpg", ".jpeg", ".ico"]:
                    if do_next == True and check in str(item_path[-6:]):
                        images.append((item, item_path, size, modification_time))
                        do_next = False
                        break
                if do_next == True:
                    files.append((item, item_path, size, modification_time))

        for item, item_path, modification_time in sorted(directories):
            tree.insert("", "end", text=item, values=(item_path, "Directory", "", format_date(modification_time)))

        for item, item_path, size, modification_time in sorted(archives):
            tree.insert("", "end", text=item, values=(item_path, "Compressed Archive", format_size(size), format_date(modification_time)))

        for item, item_path, size, modification_time in sorted(images):
            tree.insert("", "end", text=item, values=(item_path, "Image File", format_size(size), format_date(modification_time)))

        for item, item_path, size, modification_time in sorted(files):
            tree.insert("", "end", text=item, values=(item_path, "File", format_size(size), format_date(modification_time)))

        current_directory.set(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_item_select(event):
    try:
        selected_item = tree.focus()
        item_path = tree.item(selected_item, "values")[0]
        selected_item_path.set(item_path)

        if os.path.isdir(item_path):
            load_directory(item_path)
    except:
        pass


def go_up_directory():
    current_path = current_directory.get()
    parent_path = os.path.dirname(current_path)
    load_directory(parent_path)

def open_file(path):
    try:
        os.startfile(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def choose_directory():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        load_directory(selected_directory)

def delete_item():
    item_path = selected_item_path.get()
    if not item_path:
        messagebox.showwarning("Warning", "No item selected to delete.")
        return

    confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete '{os.path.basename(item_path)}'?")
    if confirm:
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                os.rmdir(item_path)

            load_directory(current_directory.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_file():
    item_path = selected_item_path.get()
    if not item_path:
        messagebox.showwarning("Warning", "No item selected to run.")
        return

    if not os.path.isfile(item_path):
        messagebox.showwarning("Warning", "Selected item is not a file.")
        return

    try:
        subprocess.Popen(item_path, shell=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

control_frame = tk.Frame(root)
control_frame.pack(fill="x")

current_directory = tk.StringVar()
directory_label = tk.Label(control_frame, textvariable=current_directory)
directory_label.pack(side="left", padx=10, pady=10)

up_button = tk.Button(control_frame, text="Up", command=go_up_directory)
up_button.pack(side="left", padx=2)

choose_button = tk.Button(control_frame, text="Choose Directory", command=choose_directory)
choose_button.pack(side="left", padx=2)

delete_button = tk.Button(control_frame, text="Delete", command=delete_item)
delete_button.pack(side="left", padx=2)

run_button = tk.Button(control_frame, text="Run", command=run_file)
run_button.pack(side="left", padx=2)

tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)

tree["columns"] = ("path", "type", "size", "date")
tree.heading("#0", text="Name")
tree.heading("path", text="Path")
tree.heading("type", text="Type")
tree.heading("size", text="Size")
tree.heading("date", text="Date")
tree.column("path", width=0, stretch=tk.NO)
tree.column("type", width=50)
tree.column("size", width=20)
tree.column("date", width=20)

tree.bind("<<TreeviewSelect>>", on_item_select)
selected_item_path = tk.StringVar()
load_directory(os.path.expanduser("~"))

root.mainloop()
