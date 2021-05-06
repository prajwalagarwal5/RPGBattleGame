from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item
from os import system, name
print("     ---------------------------------------------------------------------------------------------------------------")
print("    |"+bcolors.BOLD+bcolors.HEADER+"                                          Welcome To RPG Battle                                               "+bcolors.ENDC+"|")
print("     ---------------------------------------------------------------------------------------------------------------")

# print("\n\n")
# print("NAME            HP                                    MP")
# print("                _________________________             __________  ")
# print(bcolors.BOLD + "Valos : " +bcolors.BOLD+ "460/460|" + bcolors.OKGREEN +
#       "███████████████          " + bcolors.ENDC + bcolors.BOLD + "|      65/65|" + bcolors.OKBLUE + "██████████"+bcolors.ENDC+"|")
# print("\n\n")
# Creating black magic


fire = Spell("Fire", 70, 600, "black")
thunder = Spell("Thunder", 60, 550, "black")
blizzard = Spell("Blizzard", 40, 300, "black")
meteor = Spell("Meteor", 100, 1000, "black")
quak = Spell("Quak", 130, 1300, "black")

#Creating White Magic
cure = Spell("Cure", 90, 500, "white")
cura = Spell("Cura", 120, 600, "white")

# create some item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of the player", 9999)
# hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spell = [fire,thunder,blizzard,meteor,cure,cura]
enemy_spell = [fire,meteor, cure]
player_item = [{"item" : potion, "quantity" : 3},
               {"item" : hipotion, "quantity" : 2},
               {"item" : superpotion, "quantity" : 1},
               {"item" : elixer, "quantity" : 1},
               {"item" : grenade, "quantity" : 1}]
# enemy_item = [{"item" : potion, "quantity" : 5},
#                {"item" : hipotion, "quantity" :4},
#                {"item" : superpotion, "quantity" : 4},
#                {"item" : elixer, "quantity" : 3},
#                {"item" : hielixer,"quantity" : 2},
#                {"item" : grenade, "quantity" : 1}]
print("                        #########################################################")
print("                        #"+bcolors.BOLD+bcolors.FAIL+"  NOTE:-                                               "+bcolors.ENDC+"#")
print("                        #"+bcolors.BOLD+bcolors.FAIL+"        Number of Player should be greater than One    "+bcolors.ENDC+"#")
print("                        #"+bcolors.BOLD+bcolors.FAIL+"        Player Name should not be more than 8          "+bcolors.ENDC+"#")

print("                        ##########################################################")

number_of_players = int(input(bcolors.BOLD+"\n                     Enter number of players :- "+bcolors.ENDC))
players_name=[]
player_name=""
success=True


def set_player_name_format(name):
    while len(name) <= 8:
        name += " "
    return name

for i in range(number_of_players):
    player_name = input("\n                     Enter Name of Player" + str(i + 1)+" ")
    while success:
        count=0
        success= False

        for x in player_name:
            count+=1
        if count>8:
            print("Name cannot be more than 8 letter. Retry!!!!")
            success = True

    players_name.append(set_player_name_format(player_name))

players=[]
# mp = random.randrange(130,140)
# atk = random.randrange(200,230)
# hp = random.randrange(3200,3300)
# player_item_random = []
# Instantiate People
for i in range(number_of_players):
    # for x in range(random.randrange(0,6)):
    #     a=random.choice(player_spell)
    #     if a in player_item_random:
    #         continue
    #     else:
    #         player_item_random[i] = a
    players.append(Person(players_name[i],3200,130,100,34,player_spell,player_item))




# player1 = Person("Valos:", 3260, 132, 300, 34, player_spell, player_item)
# player2 = Person("Nick :", 4160, 188, 311, 34, player_spell, player_item)
# player3 = Person("Robot:", 3089, 174, 288, 34, player_spell, player_item)

# enemy1 = Person("Imp  ",3200*number_of_players, 130, 560, 325, enemy_spell, enemy_item)
# enemy2 = Person("Magus", 18200, 701, 525, 25, enemy_spell, enemy_item)
# enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spell, enemy_item)

# players = [player1, player2, player3]
enemies = []

defeated_players = []
defeated_enemies = []
running = True
i = 0

# print(bcolors.FAIL + bcolors.BOLD + "           AN ENEMY ATTACKS!      " + bcolors.ENDC)
while running:
    # players[0].enemy_design_upper()
    # for enemy in enemies:
    #     enemy.get_enemy_stats()
    # players[0].design_lower()

    print("")

    players[0].player_design_upper()
    for player in players:
        player.get_stats()

    players[0].design_lower()

    print("\n")

    for player in players:
        enemies.clear()
        for against in players:
            if player !=against:
                enemies.append(against)

        player.choose_action()
        choice=input("    Enter your Choice : ")
        index=int(choice)-1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(bcolors.OKBLUE + bcolors.BOLD+bcolors.UNDERLINE +player.name.strip()+bcolors.ENDC+bcolors.OKBLUE+" Player attacked Enemy " + bcolors.BOLD+
                  enemies[enemy].name.strip() +bcolors.ENDC+bcolors.OKBLUE+" for "+ str(dmg)+ " points of damage."+bcolors.ENDC)
            if enemies[enemy].get_hp() == 0:
                print(bcolors.FAIL+bcolors.BOLD+enemies[enemy].name.strip()+" has died."+bcolors.ENDC)
                defeated_enemies.append(enemies[enemy])
                j=0
                for defeat_player in players:
                    if enemies[enemy] == defeat_player:
                        del players[j]
                    j+=1


                
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Enter which magic to be applied : "))-1
            if magic_choice<0:
                continue
            spell = player.magic[magic_choice]
            cost = spell.get_spell_mp_cost()
            current_mp = player.get_mp()
            if cost>current_mp:
                print(bcolors.FAIL + "You do not Have Sufficient MP" + bcolors.ENDC)
                continue
            player.reduce_mp(cost)
            # magic_dmg = enemy.generate_spell_damage(magic_choice)
            if spell.type == "black":
                enemy = player.choose_target(enemies)
                magic_dmg = spell.generate_spell_damage()
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + bcolors.BOLD +bcolors.UNDERLINE+ player.name.strip() + bcolors.ENDC + bcolors.OKBLUE + " Player attacked Enemy " + bcolors.BOLD +
                    enemies[enemy].name.strip() + bcolors.ENDC + bcolors.OKBLUE + " with " + bcolors.BOLD + spell.name + bcolors.ENDC + bcolors.OKBLUE + " for " + str(magic_dmg) + " points of damage." + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.strip() + " has died." + bcolors.ENDC)
                    defeated_enemies.append(enemy)
                    j=0
                    for defeat_player in players:
                        if enemies[enemy] == defeat_player:
                            del players[j]
                        j += 1


            else:
                magic_heal = spell.generate_spell_heal()
                player.heal(magic_heal)
                print(bcolors.OKGREEN +bcolors.BOLD+bcolors.UNDERLINE+player.name.strip()+ bcolors.ENDC+bcolors.OKGREEN+" are healed with " +bcolors.BOLD+ spell.name + bcolors.ENDC+bcolors.OKGREEN+" for " +
                      bcolors.BOLD+str(magic_heal) +" HP."+bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice=int(input("Choose Item : "))-1
            if item_choice<0:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL+"\nNone left..."+bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN +bcolors.BOLD+bcolors.UNDERLINE+player.name.strip()+bcolors.ENDC+bcolors.OKGREEN+ " Heals for " +bcolors.BOLD+ str(item.prop), " HP."+bcolors.ENDC)

            elif item.type == "elixer":
                # if item.name == "MegaElixer":
                #     for i in players:
                #         i.hp = i.maxhp
                #         i.mp = i.maxmp
                #     print(bcolors.OKGREEN +bcolors.BOLD+ item.name +bcolors.ENDC+bcolors.OKGREEN+ " fully restored HP/MP of all the Players: " + bcolors.ENDC)
                # else:
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + bcolors.BOLD +bcolors.UNDERLINE+ player.name.strip() + bcolors.ENDC + bcolors.OKGREEN + " restored HP/MP using: " + bcolors.BOLD + item.name + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                # print(bcolors.FAIL+"\n"+ item.name+" deals ",str(item.prop)," points of damage to "+enemies[enemy].name+bcolors.ENDC)

                print(bcolors.OKBLUE + bcolors.BOLD+bcolors.UNDERLINE + player.name.strip() + bcolors.ENDC + bcolors.OKBLUE + " Player attacked Enemy " + bcolors.BOLD +
                    enemies[enemy].name.strip() + bcolors.ENDC + bcolors.OKBLUE + " using " + bcolors.BOLD +
                    item.name + bcolors.ENDC + " for " + bcolors.BOLD + bcolors.OKBLUE + str(
                        item.prop) + bcolors.ENDC + bcolors.OKBLUE + " points of damage." + bcolors.ENDC)

                # print(bcolors.OKBLUE + bcolors.BOLD + player.name + bcolors.ENDC + bcolors.OKBLUE + " Player attacked Enemy " + bcolors.BOLD +
                #     enemies[enemy].name.replace(" ", "") + bcolors.ENDC + bcolors.OKBLUE + " for " + str(
                #         item.prop) + " points of damage." + bcolors.ENDC)
                # print(bcolors.OKBLUE + "Player attacked Enemy "+enemies[enemy].name +" with " + item.name + " for " + str(
                #     item.prop) + " points of damage." + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.strip() + " has died." + bcolors.ENDC)
                    defeated_enemies.append(enemy)
                    j=0
                    for defeat_player in players:
                        if enemies[enemy] == defeat_player:
                            del players[j]
                        j += 1




    # define our clear function
    def cls():
        system('cls' if name == 'nt' else 'clear')


    if len(players)==1:
        b='N'
        print(bcolors.OKGREEN + bcolors.BOLD, "--------------"+players[0].name.strip()+" Player won!!!-------------"+ bcolors.ENDC)
        a = input("Press Any key To exit : ")
        running = False
        break
    # # check which player won
    # if defeated_enemies == 3:
    #     print(bcolors.OKGREEN+bcolors.BOLD, "--------------You won!!!-------------", bcolors.ENDC)
    #     running = False
    #     break
    #
    # print("      ===================================================")
    # print(bcolors.FAIL + "      Computer's Turn......Wait.......\n" + bcolors.ENDC)
    #
    # #enemy attack
    # for enemy in enemies:
    #     if len(enemies) == 0:
    #         break
    #     else:
    #         enemy_choice = random.randrange(0,len(enemies))
    #
    #     if enemy_choice == 0:
    #         if len(players) == 0:
    #             break
    #         else:
    #             target = random.randrange(0,len(players))
    #         enemy_dmg = enemy.generate_damage()
    #         players[target].take_damage(enemy_dmg)
    #         print(bcolors.OKBLUE + bcolors.BOLD +bcolors.UNDERLINE+ enemy.name + bcolors.ENDC + bcolors.OKBLUE + " Enemy attacked Player " + bcolors.BOLD +
    #             players[target].name.replace(" ", "") + bcolors.ENDC + bcolors.OKBLUE + " for " + str(
    #                 enemy_dmg) + " points of damage." + bcolors.ENDC)
    #         if players[target].get_hp() == 0:
    #             print(bcolors.FAIL+bcolors.BOLD+players[target].name.replace(" ","")+" has died."+bcolors.ENDC)
    #             defeated_players+=1
    #             del players[target]
    #
    #     elif enemy_choice == 1:
    #         spell = enemy.choose_enemy_spell()
    #         if spell == 1:
    #             print(bcolors.WARNING+bcolors.UNDERLINE+bcolors.UNDERLINE+enemy.name.replace(" ","")+"Enemy has used all its Magic Points.\nSo cannot Apply Magic on any Player"+bcolors.ENDC)
    #         else:
    #             magic_dmg = spell.generate_spell_damage()
    #             enemy.reduce_mp(spell.cost)
    #             if spell.type == "black":
    #                 if len(players) == 0:
    #                     target = 0
    #                 else:
    #                     target = random.randrange(0, len(players))
    #                 players[target].take_damage(magic_dmg)
    #                 print(bcolors.OKBLUE + bcolors.BOLD + bcolors.UNDERLINE+enemy.name + bcolors.ENDC + bcolors.OKBLUE + " Enemy attacked Player " + bcolors.BOLD +
    #                     players[target].name + bcolors.ENDC + bcolors.OKBLUE + " with " + bcolors.BOLD + spell.name + bcolors.ENDC + bcolors.OKBLUE + " for " + str(
    #                         magic_dmg) + " points of damage." + bcolors.ENDC)
    #                 # print(bcolors.OKBLUE + "\n" +enemy.name  + " attacked " + players[target].name +" with " + spell.name + " for " + str(
    #                 #     magic_dmg) + " points of damage." + bcolors.ENDC)
    #                 if players[target].get_hp() == 0:
    #                     print(bcolors.FAIL + bcolors.BOLD + players[target].name.replace(" ","") + " has died." + bcolors.ENDC)
    #                     defeated_players+=1
    #                     del players[target]
    #             else:
    #                 enemy.heal(magic_dmg)
    #                 print(bcolors.OKGREEN + bcolors.BOLD +bcolors.UNDERLINE+ enemy.name.replace(" ","") + bcolors.ENDC + bcolors.OKGREEN + " are healed with " + bcolors.BOLD + spell.name + bcolors.ENDC + bcolors.OKGREEN + " for " +
    #                       bcolors.BOLD + str(magic_dmg) + " HP." + bcolors.ENDC)
    #                 # print(bcolors.OKBLUE + "\n" + enemy.name + " heals using " + spell.name + " for "+str(
    #                 #     magic_dmg) + " HP." + bcolors.ENDC)
    #
    #     elif enemy_choice == 2:
    #         item = enemy.choose_enemy_item()
    #         if item.type == "potion":
    #             enemy.heal(item.prop)
    #             print(bcolors.OKGREEN +bcolors.BOLD + bcolors.UNDERLINE+enemy.name+bcolors.ENDC+bcolors.OKGREEN+ " Heals for " +bcolors.BOLD+ str(item.prop), " HP."+bcolors.ENDC)
    #
    #         elif item.type == "elixer":
    #             if item.name == "MegaElixer":
    #                 for i in players:
    #                     i.hp = i.maxhp
    #                     i.mp = i.maxmp
    #                 print(bcolors.OKGREEN +bcolors.BOLD+ item.name +bcolors.ENDC+bcolors.OKGREEN+ " fully restored HP/MP of all the Enemies: " + bcolors.ENDC)
    #             else:
    #                 player.hp = player.maxhp
    #                 player.mp = player.maxmp
    #                 print(bcolors.OKGREEN + bcolors.BOLD+bcolors.UNDERLINE+enemy.name +bcolors.ENDC+bcolors.OKGREEN+ " restored HP/MP using: "+bcolors.BOLD+item.name + bcolors.ENDC)
    #
    #         elif item.type == "attack":
    #             if len(players) == 0:
    #                 target = 0
    #             else:
    #                 target = random.randrange(0, len(players))
    #             players[target].take_damage(item.prop)
    #             print(bcolors.OKBLUE + bcolors.BOLD + bcolors.UNDERLINE+enemy.name + bcolors.ENDC + bcolors.OKBLUE + " Enemy attacked Player " + bcolors.BOLD +
    #                 players[target].name.replace(" ", "") + bcolors.ENDC + bcolors.OKBLUE + " using " +bcolors.BOLD+
    #                   item.name + bcolors.ENDC+" for "+bcolors.BOLD + bcolors.OKBLUE + str(item.prop) +bcolors.ENDC+bcolors.OKBLUE+ " points of damage." + bcolors.ENDC)
    #
    #             # print(bcolors.OKBLUE + "\n"+ enemy.name + " gave ", str(item.prop),
    #             #       " points of damage to " + players[target].name+" using "+item.name + bcolors.ENDC)
    #             # # print(bcolors.OKBLUE + "You Attacked Player - " + players[target].name + " with " + item.name + " for " + str(
    #             # #     item.prop) + " points of damage." + bcolors.ENDC)
    #             if players[target].get_hp() == 0:
    #                 print(bcolors.FAIL + bcolors.BOLD + players[target].name.replace(" ","") + " has died." + bcolors.ENDC)
    #                 defeated_players+=1
    #                 del players[target]

        # check if enemy won
    # if defeated_players == 3:
    #     print(bcolors.OKGREEN+bcolors.BOLD, "Your Enemy has defeated you", bcolors.ENDC)
    #
    #     break

    # print("-----------------------------------")
    # print("Enemy HP : "+ bcolors.FAIL + str(enemy.get_hp())+"/"+str(enemy.get_max_hp())+ bcolors.ENDC)
    # print("Your HP : " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp())+ bcolors.ENDC)
    # print("Your MP : " + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp())+ bcolors.ENDC)


    # running = False
