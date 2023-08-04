# -*- coding: utf-8 -*-


class Employee:
    def __init__(self, name, card):
        self.name = name
        self.card = card

    def clock_in(self):
        return self.card.clock_in()