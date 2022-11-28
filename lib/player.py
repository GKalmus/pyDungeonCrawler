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

      def getInfo(self):
            data = load_json()
            if not self.guildID in data:
                  data[self.guildID] = { }
                  write_json(data)
            if not self.playerID in data:
                  data[self.guildID][self.playerID] = { }
                  write_json(data)
            return data[self.guildID][self.playerID]

      def getStats(self):
            userInfo = self.getInfo()
            data = load_json()
            if not "stats" in userInfo:
                  data[self.guildID][self.playerID]["stats"] = defaultValue
                  write_json(data)
            return data[self.guildID][self.playerID]["stats"]
            
#n3gev = Player(1032256108959633448, 2661123213123423493754890)
#n3gev.getStats()