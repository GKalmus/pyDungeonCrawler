import json
import discord

def write_json(andmed:str, failinimi="../files/players.json"):
      jsonString = json.dumps(andmed, indent=4)
      with open(failinimi, "w") as f:
            f.write(jsonString)

def load_json(failinimi="../files/players.json"):
      with open(failinimi, "r") as f:
            return json.load(f)

defaultValue= {
      "health": "100", 
      "level": "1", 
      "xp": "0", 
      "attack": "1", 
      "defence": "0",
      "status": "alive"
      }


class Player:
      def __init__(self, guildID, playerID):
            self.guildID = str(guildID)
            self.playerID = str(playerID)

      def getPlayerData(self):
            playerData = self.getPlayer()
            self.health = playerData.health
            self.level = playerData.level
            self.xp = playerData.xp
            self.attack = playerData.attack
            self.defence = playerData.defence
            self.status = playerData.status

      def setPlayerData(self):
            inv = {
            "health": f"{self.health}", 
            "level": f"{self.level}", 
            "xp": f"{self.xp}", 
            "attack": f"{self.attack}", 
            "defence": f"{self.defence}",
            "status": f"{self.status}"
            }
            self.setPlayer(inv)


      def getInfo(self):
            data = load_json()
            if not self.guildID in data:
                  data[self.guildID] = { }
                  write_json(data)
            if not self.playerID in data:
                  data[self.guildID][self.playerID] = { }
                  write_json(data)
            return data[self.guildID][self.playerID]
      
      def setInfo(self, inv):
            data = load_json()
            data[self.guildID][self.playerID] = inv
            write_json(data)


      def getPlayer(self):
            inv = self.getInfo()
            data = load_json()
            if not "stats" in inv:
                  inv["stats"] = defaultValue
                  self.setPlayer(inv)
            return inv["stats"]

      def setPlayer(self, player):
            inv = self.getInfo()
            inv = player
            self.setInfo(inv)

      def damage(self, dmg):
            self.getPlayerData()
            if self.status == "Immortal":
                  dmg = 0
            else:
                  self.health = self.health - dmg
            if self.health <= 0:
                  self.health = 0
                  self.status = "Dead"
            self.setPlayerData()
            return self.health
      def heal(self, amount):
            self.getPlayerData()
            self.health += amount
            self.setPlayerData()




      
            
n3gev = Player(1032256108959633448, 2661123213123423493754890)
print(n3gev.getPlayer())