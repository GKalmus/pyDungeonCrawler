class Character:
      def write_json(andmed, failinimi):
            with open(failinimi, "w") as f:
                  json.dump(andmed, failinimi, indent=4)

      def __init__(self, health=100 , mana=10, dmg=10):
            self.health = health
            self.mana = mana
            self.dmg = dmg
            

      def damage(self, amount):
            self.health -= amount
            return amount

      def heal(self, amount):
            self.health += amount
            return amount

      def manaUse(self, amount):
            self.mana -= amount
            return amount

      def manaGet(self, amount):
            self.mana += amount
            return amountzzz

jensOlafKukk = Character(mana=50)

print(jensOlafKukk.health)
jensOlafKukk.damage(10)

print(jensOlafKukk.health)