import random



class Equipment (object):
    RARITY = ["Trash","Common","Rare","Epic","Legendary"]
    def __init__(self,eqType):
        self.rarityLevel = self.pickRare()
        self.eqType = eqType

    def pickRare(self):
        x = random.randint(1, 10)
        if x >= 1 and x <= 2:
            return Equipment.RARITY[0]
        elif x > 2 and x <= 5:
            return Equipment.RARITY[1]
        elif x > 5 and x <= 8:
            return Equipment.RARITY[2]
        elif x > 8 and x <= 9:
            return Equipment.RARITY[3]
        elif x == 10:
            return Equipment.RARITY[4]

class Armor(Equipment):
    ARMORTYPE = ["Helm", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self):
        super(Armor,self).__init__("Armor")


class Weapon(Equipment):
    WEAPONTYPE = ["Sword","Ax","Mace","Wand","Gun","Bow","Staf"]

    def __init__(self):
        super(Weapon,self).__init__("Weapon")
