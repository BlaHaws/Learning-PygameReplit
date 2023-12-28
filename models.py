class Card():
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost
        self.is_tapped = False

class Land(Card):
    def __init__(self, title):
        super().__init__(title, 0)

class Creature(Card):
    def __init__(self, title, cost, attack, defense):
        super().__init__(title, cost)
        self.attack = attack
        self.defense = defense
        self.is_tapped = False
        self.is_blocked = False
        self.is_attacking = False
        self.is_defending = False
        self.is_attacking_this_turn = False
        self.is_defending_this_turn = False
        self.is_blocked_this_turn = False

class Deck():
    cards = []
    def __init__(self):
        self.cards = []
    def add_