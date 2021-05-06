import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name=name
        self.maxhp = hp
        self.hp = hp
        self.mp=mp
        self.maxmp = mp
        self.atkl = atk - 30
        self.atkh = atk + 30
        self.df = df
        self.magic = magic
        self.items = items
        self.actions= ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal(self, heal):
        self.hp+= heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i=1
        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("        "+str(i) + ". " + item)
            i+=1

    def choose_magic(self):
        i=1
        print("\n",bcolors.OKGREEN+ bcolors.BOLD + "    Magic:" + bcolors.ENDC)
        for spell in self.magic:
            print("        "+str(i) + ". ", spell.get_spell_name()+" { cost : ", str(spell.get_spell_mp_cost())+" }")
            i+=1

    def choose_item(self):
        i=1
        print("\n",bcolors.OKGREEN + bcolors.BOLD + "    Items:" + bcolors.ENDC)
        for items in self.items:
            print("        " , str(i) , ". ", items["item"].name, " : ", items["item"].description, " Quantity : (x"+str(items["quantity"])+")")
            i+=1

    def choose_target(self,enemies):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            print("        " + str(i) +".",enemy.name)
            i+=1
        choice = int(input("    Choose Target : ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("        #                              __________________________________________________        #")
        print("        #          "+bcolors.BOLD + self.name + "   " + bcolors.BOLD + current_hp + "|" + bcolors.FAIL +
              hp_bar +bcolors.ENDC+"|       #" )
    def get_stats(self):
        hp_bar = ""
        mp_bar = ""

        bar_ticks = (self.hp/self.maxhp)*100/4
        while bar_ticks>0:
            hp_bar+="█"
            bar_ticks-=1
        while len(hp_bar)<25:
            hp_bar+=" "
        bar_ticks = (self.mp/self.maxmp)*100/10

        while bar_ticks > 0:
            mp_bar += "█"
            bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        hp_string = str(self.hp)+"/"+str(self.maxhp)
        mp_string = str(self.mp)+"/"+str(self.maxmp)
        current_mp = ""
        current_hp = ""
        if len(hp_string)<9:
            decreased = 9 - len(hp_string)
            while decreased>0:
                current_hp+=" "
                decreased-=1
            current_hp+=hp_string
        else:
            current_hp = hp_string

        if len(mp_string)<9:
            decreased = 7 - len(mp_string)
            while decreased>0:
                current_mp+=" "
                decreased-=1
            current_mp+=mp_string
        else:
            current_mp = mp_string



        print("            #                             _________________________               __________         #")
        print("            #          "+bcolors.BOLD + self.name+ bcolors.BOLD + current_hp+"|" + bcolors.OKGREEN +
              hp_bar + bcolors.ENDC + bcolors.BOLD + "|      "+current_mp+"|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|        #")

    def choose_enemy_spell(self,breakpoint1=5):
       if breakpoint1 == 0:
            return 1
       magic_choice = random.randrange(0, len(self.magic))
       spell = self.magic[magic_choice]
       pct = self.hp/self.maxhp*100

       if self.mp<spell.cost or spell.type == "white" and pct>50:
           return self.choose_enemy_spell(breakpoint1-1)
       else:
           return spell

    def enemy_design_upper(self):
        print("            ##########################################################################################")
        print("            #                              #  Enemy's Details  #                                     #")
        print("            #                              #####################                                     #")
        print("            #          NAME               HP                                                         #")

    def design_lower(self):
        print("            #                                                                                        #")
        print("            ##########################################################################################")

    def player_design_upper(self):
        print("            ##########################################################################################")
        print("            #                              # Player's Details  #                                     #")
        print("            #                              #####################                                     #")

        print("            #          NAME               HP                                      MP                 #")


    def choose_enemy_item(self):

        item_choice=random.randrange(0,len(self.items))
        item = self.items[item_choice]
        # pct = self.maxhp / self.maxhp * 100
        if item["quantity"] == 0:
            return self.choose_enemy_item()
        else:
            item["quantity"] -= 1
            return item["item"]

    def set_player_name_format(self,name):
        while len(name)<=7:
            name+=" "
        return name

