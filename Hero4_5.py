import random

class Hero(object):
    RACELIST = ["Human","Elf","Dwarf","Dog"]
    CLASSLIST = ["Warrior","Mage","Hunter","Dog"]

    def __init__(self):
        # class setup String values
        self.isAlive = True
        self.level = 1
        self.race = self.pickRace()
        self.playerClass = self.pickClass()
        self.name = self.enterName()
        # class setup starting XP and leveling vallues
        self.xp = 0
        self.xpToLevelUp = 90 + (self.level * 10)
        # hero health initial setup
        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.healAct = self.maxHealth
        # hero Mana inatial setup
        self.manaMod = 10
        self.maxmana = self.level * self.manaMod
        self.manaAct = self.maxmana
        # hero stat modifiers
        self.deff = 0
        self.atk = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
        # seting base values based on class and race
        self.setMods()

        #setup hero inventorys
        self.inventory = ["test"]
        self.invmax = 10
        self.helmeq = []
        self.chesteq = []
        self.legeq = []
        self.gloveseq = []
        self.bootseq = []
        self.righthandwep = []
        self.lefthandwep = []



    def setMods(self):
        #this method sets the starting modifyer values for your hero
        if self.playerClass == "Warrior":
            self.deff = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxmana = 0
        if self.playerClass == "Mage":
            self.deff = random.randint(5, 10)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.manaMod = random.randint(15,20)
        if self.playerClass == "Hunter":
            self.deff = random.randint(5, 15)
            self.atk = random.randint(8, 18)
            self.luck = random.randint(5, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(5, 15)
        if self.playerClass == "Dog":
            self.deff = random.randint(90,100)
            self.atk = 100
            self.luck = 100
            self.stamina = 100
            self.iq = 100
            self.agi = 100
        if self.race == "Elf":
            self.stamina -= 2
            self.iq += 2
        if self.race == "Dwarf":
            self.stamina += 2
            self.iq -= 2
        if self.race == "Dog":
            self.atk += 10
            self.deff += 10
            self.luck += 10
            self.stamina += 10
            self.iq += 10
            self.agi += 10

    def __str__(self):
        # provides a String representation of the object
        return """
        Name: {} \t Race: {} \t Class: {} \t Level: {}
        Health: {} \t Mana: {} \t Xp: {}
        Atack: {} \t Deffence: {}
        Luck: {} \t Stamina: {}
        IQ: {}     \t Agility: {}
        """.format(self.name, self.race, self.playerClass, self.level, self.healAct, self.manaAct, self.xp, self.atk,
                   self.deff, self.luck, self.stamina, self.iq, self.agi)

    def pickRace(self):
        # allows us to pick our race from the class race list
        while True:
            try:
                print(Hero.RACELIST)
                x = input("pick your Race")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a good option")

    def pickClass(self):
        # allows us to pick our class from the class list
        while True:
            try:
                print(Hero.CLASSLIST)
                x = input("pick your Race")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a good option")

    def enterName(self):
        # lets us set up our hero's name
        name = ""
        while name == "":
            name = input("What would you like to name this character")
        return name

    def die(self):
        if self.healAct <= 0:
            self.isAlive = False
            dropXp = 10 * self.level
            dropitem = random.choice(self.inventory)
            return dropXp, dropitem

        else:
            return "",""

    def levelUp(self):

        if self.xp >= self.xpToLevelUp:
            print("Ding Level up")
            print(self)
            remxp = self.xp - self.xpToLevelUp
            self.level += 1
            self.xpToLevelUp = 90 + (self.level * 10)
            self.xp = remxp

            self.healthMod = self.healthMod + self.level
            self.maxHealth = self.level * self.healthMod
            self.healAct = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod = self.manaMod + self.level
                self.maxmana = self.level * self.manaMod
                self.manaAct = self.maxmana
            self.levelMod()
        else:
            return

    def levelMod(self):
        points = random.randint(1, self.level+1)
        while points > 0:
            print(
                """Luck: {}
                Stamina: {}
                IQ: {}
                Agility: {}""".format(self.luck, self.stamina, self.iq, self.agi))
            x = input("what Stat would you like to add points to")
            y = int(input(self.name+" you have " + str(points) + " points to spend how many would you like to put in " + x))
            if x == "Stamina":
                self.stamina += y
                points -= y
            elif x == "Luck":
                self.luck += y
                points -= y
            elif x == "IQ":
                self.iq += y
                points -= y
            elif x == "Agility":
                self.agi += y
                points -= y
            else:
                print("not an option")

    def collectXp(self,xp):
        print("you picked up "+str(xp)+"xp")
        self.xp += xp
        self.levelUp()

    def attack(self):
        pass

    def defend(self):
        pass

    def equipHead(self):
        pass

    def equipChest(self):
        pass

    def equipLegs(self):
        pass

    def equipBoots(self):
        pass

    def equipGloves(self):
        pass

    def addToInv(self):
        pass

    def removeFromInv(self):
        pass

    def useHpPotion(self):
        pass

    def useMpPotion(self):
        pass



