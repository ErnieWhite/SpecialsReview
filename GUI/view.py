import tkinter as tk
from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create all the widgets to load the data files ######################
        self.file_control_frame = ttk.Label(self)
        self.file_control_frame.pack()
        # create the customer special file load widgets
        self.load_customer_label = ttk.Label(self.file_control_frame, text='Customer Specials')
        self.load_customer_entry = ttk.Entry(self.file_control_frame)
        self.load_customer_button = ttk.Button(self.file_control_frame, text='Load')
        self.load_customer_label.grid(row=0, column=0, sticky='w')
        self.load_customer_entry.grid(row=0, column=1)
        self.load_customer_button.grid(row=0, column=2)

        # create the branch special file load widgets
        self.load_branch_label = ttk.Label(self.file_control_frame, text='Branch Specials')
        self.load_branch_entry = ttk.Entry(self.file_control_frame)
        self.load_branch_button = ttk.Button(self.file_control_frame, text='Load')
        self.load_branch_label.grid(row=1, column=0, sticky='w')
        self.load_branch_entry.grid(row=1, column=1)
        self.load_branch_button.grid(row=1, column=2)

        # create the rate_card special file load widgets
        self.load_rate_card_label = ttk.Label(self.file_control_frame, text='Rate Cards')
        self.load_rate_card_entry = ttk.Entry(self.file_control_frame)
        self.load_rate_card_button = ttk.Button(self.file_control_frame, text='Load')
        self.load_rate_card_label.grid(row=2, column=0, sticky='w')
        self.load_rate_card_entry.grid(row=2, column=1)
        self.load_rate_card_button.grid(row=2, column=2)

        # create the notebook to hold our three tables #######################
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True)
        self.cs_frame = ttk.Frame(self.notebook)
        self.bs_frame = ttk.Frame(self.notebook)
        self.rc_frame = ttk.Frame(self.notebook)
        self.cs_frame.pack(expand=True)
        self.bs_frame.pack(expand=True)
        self.rc_frame.pack(fill=tk.Y)
        # add x-scrollbars
        self.cs_x_scrollbar = ttk.Scrollbar(self.cs_frame, orient=tk.HORIZONTAL)
        self.bs_x_scrollbar = ttk.Scrollbar(self.bs_frame, orient=tk.HORIZONTAL)
        self.rc_x_scrollbar = ttk.Scrollbar(self.rc_frame, orient=tk.HORIZONTAL)
        self.cs_x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.bs_x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.rc_x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # add y-scrollbars
        self.cs_y_scrollbar = ttk.Scrollbar(self.cs_frame, orient=tk.VERTICAL)
        self.bs_y_scrollbar = ttk.Scrollbar(self.bs_frame, orient=tk.VERTICAL)
        self.rc_y_scrollbar = ttk.Scrollbar(self.rc_frame, orient=tk.VERTICAL)

        self.cs_y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bs_y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.rc_y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cs_treeview = ttk.Treeview(
            self.cs_frame,
            yscrollcommand=self.cs_y_scrollbar.set,
            xscrollcommand=self.cs_x_scrollbar.set
        )
        self.bs_treeview = ttk.Treeview(
            self.bs_frame,
            yscrollcommand=self.bs_y_scrollbar.set,
            xscrollcommand=self.bs_x_scrollbar.set
        )
        self.rc_treeview = ttk.Treeview(
            self.rc_frame,
            yscrollcommand=self.rc_y_scrollbar.set,
            xscrollcommand=self.rc_x_scrollbar.set
        )
        self.cs_treeview.pack()
        self.bs_treeview.pack()
        self.rc_treeview.pack()

        self.notebook.add(self.cs_frame, text='Customer Specials')
        self.notebook.add(self.bs_frame, text='Branch Specials')
        self.notebook.add(self.rc_frame, text='Rate Cards')

        self.grid(row=0, column=0)
