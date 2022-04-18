import tkinter as tk
from tkinter import filedialog as fd
import csv


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.setup_event_handlers()
        self.setup_control_variables()

    def setup_control_variables(self):
        self.view.load_customer_entry['textvariable'] = self.model.customer_specials_filename
        self.view.load_branch_entry['textvariable'] = self.model.branch_specials_filename
        self.view.load_rate_card_entry['textvariable'] = self.model.rate_cards_filename

    def setup_event_handlers(self):
        self.view.load_customer_button['command'] = self.load_customer_specials_data
        self.view.load_branch_button['command'] = self.load_branch_specials_data
        self.view.load_rate_card_button['command'] = self.load_rate_cards_data

    def load_customer_specials_data(self):
        filetypes = (('csv files', '*.csv'),)

        filename = fd.askopenfilename(
            title='Open Customer Specials File',
            initialdir='/',
            filetypes=filetypes)

        self.model.customer_specials_filename.set(filename)
        self.model.customer_specials = self.get_csv_special_data(self.model.customer_specials_filename.get())

    def load_branch_specials_data(self):
        filetypes = (('csv files', '*.csv'),)

        filename = fd.askopenfilename(
            title='Open Branch Specials File',
            initialdir='/',
            filetypes=filetypes)

        self.model.branch_specials_filename.set(filename)
        self.model.branch_specials = self.get_csv_special_data(self.model.branch_specials_filename.get())

    def load_rate_cards_data(self):
        filetypes = (('csv files', '*.csv'),)

        filename = fd.askopenfilename(
            title='Open Rate Card File',
            initialdir='/',
            filetypes=filetypes)

        self.model.rate_cards_filename.set(filename)
        self.model.rate_cards = self.get_csv_rate_card_data(self.model.rate_cards_filename.get())
        self.view.rc_treeview['columns'] = list(self.model.rate_cards_header)
        self.view.rc_treeview['show'] = 'headings'
        for heading in self.model.rate_cards_header:
            self.view.rc_treeview.heading(heading, text=heading)
        for k, v in self.model.rate_cards:
            for row in v.values():
                self.view.rc_treeview.insert('', tk.END, values=row)
        print(self.model.rate_cards_header)

    @staticmethod
    def get_csv_special_data(f: str):
        """Load the data in f into a dictionary"""

        d = dict()
        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                key = ':'.join([row['Branch/Terr.'], row['Customer ID'], row['PROD_NBR']])
                d[key] = d.get(key, []) + [row]
        return d

    @staticmethod
    def get_csv_rate_card_data(f: str):
        """Load the data in f into a dictionary"""

        d = dict()
        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                key = ':'.join([row['Branch/Terr.'], row['Customer Class'], row['PROD_NBR']])
                d[key] = d.get(key, []) + [row]
        return d
