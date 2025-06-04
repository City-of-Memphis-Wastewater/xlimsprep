import tkinter as tk
from tkinter import ttk
import pandas as pd
from pathlib import Path

class CSVViewerApp:
    def __init__(self, root, folder):
        self.root = root
        self.root.title("CSV Viewer")
        self.folder = Path(folder)
        self.csv_files = sorted(self.folder.glob("*.csv"))
        self.index = 0

        # Frame to hold tree and scrollbars
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(expand=True, fill="both")

        self.tree = ttk.Treeview(self.tree_frame, show="headings")
        self.tooltip = ToolTip(self.tree)
        self.tree.bind("<Motion>", self.on_tree_hover)
        self.tree.bind("<Leave>", lambda e: self.tooltip.hidetip())
        self.tree.pack(side="left", expand=True, fill="both")

        # Scrollbars
        self.v_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.h_scroll = ttk.Scrollbar(root, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.v_scroll.pack(side="right", fill="y")
        self.h_scroll.pack(fill="x")

        # Navigation buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.prev_button = tk.Button(self.button_frame, text="← Previous", command=self.prev_file)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next →", command=self.next_file)
        self.next_button.grid(row=0, column=1, padx=10)

        self.label = tk.Label(root, text="")
        self.label.pack()

        # Keyboard bindings
        self.root.bind("<Left>", lambda event: self.prev_file())
        self.root.bind("<Right>", lambda event: self.next_file())

        self.load_csv()
        
    def on_tree_hover(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "heading":
            column_id = self.tree.identify_column(event.x)
            col_index = int(column_id.replace("#", "")) - 1
            if 0 <= col_index < len(self.tree["columns"]):
                col_name = self.tree["columns"][col_index]
                x = event.x_root + 10
                y = event.y_root + 10
                self.tooltip.showtip(col_name, x, y)
        else:
            self.tooltip.hidetip()

    def load_csv(self):
        if not self.csv_files:
            self.label.config(text="No CSV files found.")
            return

        csv_path = self.csv_files[self.index]
        self.label.config(text=csv_path.name)

        df = pd.read_csv(csv_path)

        # Clear tree
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center", stretch=True)

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def prev_file(self):
        self.index = (self.index - 1) % len(self.csv_files)
        self.load_csv()

    def next_file(self):
        self.index = (self.index + 1) % len(self.csv_files)
        self.load_csv()
        
class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.text = ""

    def showtip(self, text, x, y):
        self.text = text
        if self.tipwindow or not self.text:
            return
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root, folder="exports")
    root.mainloop()
