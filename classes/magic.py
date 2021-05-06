import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name=name
        self.cost=cost
        self.dmg=dmg
        self.type=type

    def generate_spell_damage(self):
        mgl = self.dmg - 30
        mgh = self.dmg + 30
        return random.randrange(mgl, mgh)

    def generate_spell_heal(self):
        mgl = self.dmg - 5
        mgh = self.dmg + 5
        return random.randrange(mgl, mgh)

    def get_spell_name(self):
        return self.name

    def get_spell_mp_cost(self):
        return self.cost

