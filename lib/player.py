## Autor: Gert Kalmus

import json

def write_json(andmed:str, failinimi="../files/players.json"):
      jsonString = json.dumps(andmed, indent=4)
      with open(failinimi, "w", encoding="UTF-8") as f:
            f.write(jsonString)

def load_json(failinimi="../files/players.json"):
      with open(failinimi, "r", encoding="UTF-8") as f:
            return json.load(f)

defaultValue= {
      "name": "name",
      "health": "100", 
      "level": "1", 
      "xp": "0", 
      "attack": "1", 
      "defence": "0",
      "status": "Alive"
      }

itemDefaultValue= {
      "id": "",
      "name": "",
      "propeties": {},
      "lore": ""
      }


class Player:
      def __init__(self, playerID):
            self.playerID = str(playerID)
            self.getPlayerData()
            self.inventory = self.getInv()
            self.getXp()
            
      def getInfo(self):
            data = load_json()
            if not self.playerID in data:
                  data[self.playerID] = { }
                  write_json(data)
            return data[self.playerID]
      
      def setInfo(self, info):
            data = load_json()
            data[self.playerID] = info
            write_json(data)

      def getPlayer(self):
            playerInfo = self.getInfo()
            if not "player" in playerInfo:
                  player = defaultValue
                  self.setPlayer(player)
                  playerInfo = self.getInfo() # Uuendab playerInfot
            return playerInfo["player"]
      
      def setPlayer(self, player):
            playerInfo = self.getInfo()
            playerInfo["player"] = player
            self.setInfo(playerInfo)
      
      def getInv(self):
            playerInfo = self.getInfo()
            if not "inventory" in playerInfo:
                  inv = {"backpack":{},"equip":{}}
                  self.setInv(inv)
                  playerInfo = self.getInfo() # Uuendab playerInfot
            return playerInfo["inventory"]

      def setInv(self, inv):
            playerInfo = self.getInfo()
            playerInfo["inventory"] = inv
            self.setInfo(playerInfo)

      def getBackpack(self): #
            inv = self.getInv()
            return inv["backpack"]
      
      def setBackpack(self, backpack):
            inv = self.getInv()
            inv["backpack"] = backpack
            self.setInv()

      def getEquip(self):
            inv = self.getInv()
            return inv["equip"]
      
      def setEquip(self, equip):
            inv = self.getInv()
            inv["equip"] = equip
            self.setInv()

      def getPlayerData(self):
            playerData = self.getPlayer()
            self.name = playerData["name"]
            self.health = int(playerData["health"])
            self.level = int(playerData["level"])
            self.xp = int(playerData["xp"])
            self.attack = int(playerData["attack"])
            self.defence = int(playerData["defence"])
            self.status = playerData["status"]

      def setPlayerData(self):
            inv = {
            "name": f"{self.name}",
            "health": f"{int(self.health)}", 
            "level": f"{int(self.level)}", 
            "xp": f"{int(self.xp)}", 
            "attack": f"{int(self.attack)}", 
            "defence": f"{int(self.defence)}",
            "status": f"{self.status}"
            }
            self.setPlayer(inv)

      def setName(self, name):
            self.getPlayerData()
            self.name = name
            self.setPlayerData()

      def levelUp(self):
            self.level += 1
            self.health = self.level*self.level+100
            if self.level%5== 0:
                  self.attack += 1
                  self.defence += 5
      
      def getXp(self, incomingXp:str= 0):
            self.getPlayerData()
            level = self.level
            self.xp += incomingXp
            if self.xp >= (level*level*100):
                  while self.xp >= (level*level*100):
                        self.xp -= level*level*100
                        self.levelUp()
            self.setPlayerData()
            return self.xp

      def setAttack(self, amount):
            self.getPlayerData()
            self.attack = amount
            self.setPlayerData()

      def setDefence(self, amount):
            self.getPlayerData()
            self.defence = amount
            self.setPlayerData()

      def damage(self, dmg):
            self.getPlayerData()
            end = True
            if self.status == "Immortal":
                  dmg = 0
            else:
                  self.health = self.health - dmg
            if self.health <= 0:
                  self.health = 0
                  self.status = "Dead"
                  end = False
            self.setPlayerData()
            return end

      def setHealth(self, amount):
            self.getPlayerData()
            self.health = amount
            self.setPlayerData()
      
      def revive(self):
            self.getPlayerData()
            level = self.level
            if self.status == "Dead":
                  self.health = level*level+100
                  self.status = "Alive"
                  self.setPlayerData()
                  return True
            else:
                  return False



