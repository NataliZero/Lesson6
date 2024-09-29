from abc import ABC, abstractmethod


# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def fight(self):
        return self.weapon.attack()


# Шаг 4: Создаем класс Monster и реализация боя
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self):
        self.health -= 10
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return f"У монстра осталось {self.health} здоровья."


# Инициализация персонажей
fighter = Fighter(Sword())
monster = Monster(20)

# Боец атакует монстра
print(fighter.fight())
print(monster.take_damage())

# Боец меняет оружие на лук и снова атакует
fighter.change_weapon(Bow())
print(fighter.fight())
print(monster.take_damage())
