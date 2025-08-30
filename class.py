   #ACTIVITY 1
class Smartphone:
    def _init_(self, brand, model, storage, battery):
    
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

def call(self, number):
        return f"Calling {number} from {self.model} 📞"

def charge(self, amount):
        self.battery += amount
        return f"Battery charged to {self.battery}% 🔋"

class GamingPhone(Smartphone):
    def _init_(self, brand, model, storage, battery):
          self.brand = brand
          self.model = model
          self.storage = storage
          self.battery = battery
        

phone1 = Smartphone("Samsung", "Galaxy A05", "64GB", 13)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", "512GB", 90, "liquid")

print(phone1.call("123-456-789"))
print(phone1.charge(10))
print(gaming_phone.play_game("PUBG")) 

       #ACTIVITY 2
class Animal:
    def move(self):
        pass


class Dog:
    def move(self):
        return "The dog runs"


class Bird:
    def move(self):
        return "The bird flies"


class Fish:
    def move(self):
        return "The fish swims"

for animals in [Dog(), Bird(), Fish()]:
    print(animals.move())