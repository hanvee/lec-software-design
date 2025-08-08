from abc import ABC, abstractmethod

# Abstract base class
class GameCharacter(ABC):
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def take_damage(self, amount: int):
        self.hp -= amount
        print(f"{self.name} took {amount} damage. Remaining HP: {self.hp}")

    @abstractmethod
    def attack(self):
        pass


# Warrior subclass
class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} swings a sword with great force!")


# Archer subclass
class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} shoots a precise arrow!")


# Mage subclass
class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} casts a powerful fireball!")


# Simulation
def run_game():
    characters = [
        Warrior("Stark", 100),
        Archer("Wolf", 80),
        Mage("Frieren", 70)
    ]

    print("\n=== Characters Attacking ===")
    for char in characters:
        char.attack()

    print("\n=== Damage Simulation ===")
    characters[0].take_damage(20)
    characters[1].take_damage(30)
    characters[2].take_damage(25)


if __name__ == "__main__":
    run_game()
