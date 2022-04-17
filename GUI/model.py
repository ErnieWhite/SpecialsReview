import tkinter as tk


class Model:
    def __init__(self):
        self.customer_specials_filename = tk.StringVar()
        self.branch_specials_filename = tk.StringVar()
        self.rate_cards_filename = tk.StringVar()
        self.customer_specials = {}
        self.branch_specials = {}
        self.rate_cards = {}

    @property
    def customer_specials_filename(self):
        return self.__customer_specials_filename

    @customer_specials_filename.setter
    def customer_specials_filename(self, name):
        self.__customer_specials_filename = name

    @property
    def branch_specials_filename(self):
        return self.__branch_specials_filename

    @branch_specials_filename.setter
    def branch_specials_filename(self, name):
        self.__branch_specials_filename = name

    @property
    def rate_cards_filename(self):
        return self.__rate_cards_filename

    @rate_cards_filename.setter
    def rate_cards_filename(self, name):
        self.__rate_cards_filename = name

    @property
    def branch_specials(self):
        return self.__branch_specials

    @branch_specials.setter
    def branch_specials(self, data):
        self.__branch_specials = data

    @property
    def customer_specials(self):
        return self.__customer_specials

    @customer_specials.setter
    def customer_specials(self, data):
        self.__customer_specials = data

    @property
    def rate_cards(self):
        return self.__rate_cards

    @rate_cards.setter
    def rate_cards(self, data):
        self.__rate_cards = data

    @property
    def rate_cards_header(self):
        return self.__rate_cards[list(self.__rate_cards.keys())[0]][0].keys()
