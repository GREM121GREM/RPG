import random
import time

class Player:
    def __init__(self, player_name, player_hp, player_damage):
        self.name = player_name
        self.hp = player_hp
        self.damage = player_damage
        self.lvl = 1
        self.exp = 0
    def lvl_up(self):
        self.lvl += 1
        self.exp = 0
        self.hp += 15*self.lvl
        self.damage += 10*self.lvl
        print(f"Поздравляем, у вас новый уровень! {self.lvl}\n"
              f"HP Увеличено на {15*self.lvl}\n"
              f"Ваш урон увеличен на {10*self.lvl}")
    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = 0
        damage = 0
        name = player_name
        if player_race == races_list[0]:
            hp += 240
            damage += 3000
        elif player_race == races_list[1]:
            hp += 220
            damage += 35
        elif player_race == races_list[2]:
            hp += 260
            damage += 25
        elif player_race == races_list[3]:
            hp += 300
            damage += 20
        else:
            print("Неверно: Раса или Класс")
            quit()

        if player_class == class_list[0]:
            hp += 15
            damage += 5
        elif player_class == class_list[1]:
            hp += 30
            damage -= 5
        elif player_class == class_list[2]:
            hp -= 20
            damage += 10
        else:
            print("Неверно: Раса или Класс")
        return Player(name, hp, damage)

    @staticmethod
    def weapon():
        weapon_type = ["Сковородка", "Бита", "Арбалет", "Посох", "Копьё", "Лопата"]
        weapon_rare = {
            1: "Обычный",
            1.5: "Необычный",
            2: "Редкий",
            2.5: "Эпический",
            3: "Легендарный",
            5: "Мифический"
        }
        shanse = random.randint(0, 100)
        weapon = None
        rare = None
        if 0 <= shanse <= 30:
            weapon = weapon_type[0]
        elif shanse >= 31 and shanse <= 51:
            weapon = weapon_type[1]
        elif shanse >= 52 and shanse <= 57:
            weapon = weapon_type[5]
        elif shanse >= 58 and shanse <= 80:
            weapon = weapon_type[3]
        elif shanse >= 81 and shanse <= 96:
            weapon = weapon_type[4]
        elif shanse >= 97 and shanse <= 100:
            weapon = weapon_type[2]
        else:
            print("Ошибка!")

        shanse_rare = random.randint(0, 100)

        if shanse_rare >= 0 and shanse_rare <= 30:
            rare = 1
        elif shanse_rare >= 31 and shanse_rare <= 61:
            rare = 1.5
        elif shanse_rare >= 62 and shanse_rare <= 77:
            rare = 2
        elif shanse_rare >= 78 and shanse_rare <= 89:
            rare = 2.5
        elif shanse_rare >= 90 and shanse_rare <= 97:
            rare = 3
        elif shanse_rare >= 98 and shanse_rare <= 100:
            rare = 5
        else:
            print("Ошибка!")

        if weapon == weapon_type[0]:
            perc.damage += 5 * rare
        elif weapon == weapon_type[1]:
            perc.damage += 8 * rare
        elif weapon == weapon_type[2]:
            perc.damage += 20 * rare
        elif weapon == weapon_type[3]:
            perc.damage += 12 * rare
        elif weapon == weapon_type[4]:
            perc.damage += 17 * rare
        elif weapon == weapon_type[5]:
            perc.damage += 20 * rare
        else:
            print("Ошибка!")
        return weapon, weapon_rare[rare]
    @staticmethod
    def heal():
        heal = ["Бинт", "Аптечка", "Яблоко"]
        heal_rare = [4, 2.7, 7]
        heal_random = random.choices(heal, weights=heal_rare, k=1)
        if heal_random[0] == heal[0]:
            perc.hp += 15
        elif heal_random[1] == heal[1]:
            perc.hp += 100
        elif heal_random[2] == heal[2]:
            perc.hp += 5
        else:
            print("Ошибка!")

        return heal_random[0]


    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Вы нанесли урон: {self.damage}.")
        time.sleep(1)
        if victim.hp <= 0:
            random_exp = random.randint(5,15)*self.lvl
            print(f"Поздравляем, {victim.name} повержен! + {random_exp} опыта.")

            predmet = (0, 1, 2)
            vibor = random.choice(predmet)
            if vibor == 1:
                weapon = self.weapon()
                print(f"Вам выпало оружие:\n"
                      f"{weapon[0]}, редкость {weapon[1]} "
                      f"ваш урон: {self.damage}")
            elif vibor == 0:
                pass
            elif vibor == 2:
                heal = self.heal()
                print(f"Вы получили: {heal}\n"
                      f"Ваше HP {self.hp}")
            else:
                print("Ошибка")

            self.exp += random_exp
            max_exp = 100*self.lvl
            if self.exp >= max_exp:
                self.lvl_up()
                time.sleep(1)
                max_exp = 100 * self.lvl
                print(f"До следущего уровня: {max_exp} опыта.")
            time.sleep(1)
            return False
        elif victim.hp > 0:
            print(f"{victim.name}, осталось здоовья {victim.hp}.")
            time.sleep(1)
            return True

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    @staticmethod
    def create_enemy():
        enemy_names = ["Skelet", "Vampir", "Roshan", "Pudge"]
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(200, 260) + 40*perc.lvl
        enemy_damage = random.randint(30, 40) + 10*perc.lvl
        return Enemy(enemy_name, enemy_hp, enemy_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name}, нанес урон:{self.damage}.")
        time.sleep(1)
        if victim.hp <= 0:
            print("Вы повержены, игра окончена.")
            quit()
        elif victim.hp > 0:
            print(f"Ваше здоровье: {victim.hp}.")
            time.sleep(1)


races_list = ["эльф", "гном", "хоббит", "человек"]
class_list = ["лучник", "рыцарь", "маг"]

print("Привет, как тебя зовут?")
name = input()

print("Выберите расу")
for i in races_list:
    print(i, end=" ")
print()
player_race = input().lower().replace(" ","")

print("Выберите класс")
for i in class_list:
    print(i, end=" ")
print()
player_class = input().lower().replace(" ","")

perc = Player.create_player(name, player_race, player_class)


print(f"Ваше имя {perc.name},ваш HP {perc.hp},ваш DAMAGE {perc.damage}")
time.sleep(1.5)


def fight_choice():
    print("Атаковать(1) или Сбежать(2)?")
    answer = input()
    try:
        answer = int(answer)
    except ValueError:
        print("Нельзя вводить буквы!")
    if answer == 1:
        fight = perc.attack(enemy)
        if fight:
            enemy.attack(perc)
            fight_choice()

    elif answer == 2:
        run = [1, 0]
        run_away = random.choice(run)
        if run_away == 1:
            print("Пока вы убегали, вам встретилось 2 пути, куда пойдёте?\n"
                  "Налево(1), Направо(2)")
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                   print("Нельзя вводить буквы!")
            if choice == 1:
                left = (1, 0)
                left_choice = random.choice(left)
                if left_choice == 1:
                    print("Вы сбежали.")
                elif left_choice == 0:
                    print("Вы в тупике, вас поймали!")
                    enemy.attack(perc)
                    fight_choice()
            elif choice == 2:
                right = (1, 0)
                right_choice = random.choice(right)
                if right_choice == 1:
                    print("Вы сбежали.")
                elif right_choice == 0:
                    print("Вы в тупике, вас поймали!")
                    enemy.attack(perc)
                    fight_choice()
            else:
                print("Ошибка! Введите 1 или 2")
                fight_choice()
        elif run_away == 0:
            print("Вас поймали!")
            enemy.attack(perc)
            fight_choice()
    else:
        print("Ошибка введите 1 или 2")
        fight_choice()


while True:
    event = random.randint(0,1)
    if event == 0:
        print("Вы никого не встретили, идём дальше...")
        time.sleep(1.5)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f"Вас заметил {enemy.name},\n"
              f"Урон: {enemy.damage}\n"
              f"HP: {enemy.hp}")
        fight_choice()
    else:
        print("Ошибка!")

