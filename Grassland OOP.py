import random

class Box:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.food = []
        self.grass = []
        self.water = []
        self.human = False

    def place(self, animal):
        self.food.append(animal)
        animal.location = (self.x, self.y)

    def take(self, animal):
        self.food.remove(animal)

    def move_all(self, Map):
        for i in self.food:
            self.take(i)
            Map[(random.randint(0,2), random.randint(0,1))].place(i)
        
class Grass:
    def __init__(self, value):
        self.name = "Grass"
        self.value = value
        
class Rock:
    def __init__(self, damage):
        self.name = "Rock"
        self.damage = damage

    def cut(self, animal):
        if (random.random() < (animal.legs * 0.2)):
            animal.hp -= self.damage
        
class WaterSource:
    def __init__(self, amount):
        self.name = "Water"
        self.amount = amount

    def increase_water(self, value):
        self.amount += value
        
class Animal:
    def __init__(self, name, value, legs):
        self.hp = 100
        self.thirst = 0
        self.hunger = 0
        self.value = value
        self.name = name
        self.legs = legs
        self.location = ()

    def move(self, Map, x, y):
        Map[self.location].take(self)
        Map[(x, y)].place(self)
        
    def increase_hunger(self):
        self.hunger += 5

    def increase_thirst(self):
        self.thirst += 10

    def decrease_hp(self):
        if (self.hunger >= 100):
            self.hp -= 40
        elif (self.hunger >= 80):
            self.hp -= 10            
        elif (self.hunger >= 50):
            self.hp -= 5
        
        if (self.thirst >= 100):
            self.hp -= 50    
        elif (self.thirst >= 80):
            self.hp -= 10            
        elif (self.thirst >= 50):
            self.hp -= 5
       
        if (self.hp > 0 and self.hp < 50):
            print(self.name + " is about to die")
            
    def check_alive(self):
        if (self.hp > 0):
            return True
        else:
            return False

    def drink(self, water, amount):
        if (water.amount < amount):
            amount = water.amount
        self.thirst -= amount
        water.amount -= amount

    def eat(self, food):
        self.hunger = max(0, self.hunger - food.value)
        
class Carnivore(Animal):
    def __init__(self, name, value, legs):
        super().__init__(name, value, legs)

    def decrease_hp(self):
        super().decrease_hp()

    def eat(self, food):
        if (isinstance(food, Animal)):
            super().eat(food)
        else:
            print(self.name + " cannot eat " + food.name)
            
class Herbivore(Animal):
    def __init__(self, name, value, legs):
        super().__init__(name, value, legs)

    def decrease_hp(self):
        super().decrease_hp()

    def eat(self, food):
        if (isinstance(food, Grass)):
            super().eat(food)
        else:
            print(self.name + " cannot eat " + food.name)
            
class Omnivore(Carnivore, Herbivore):
    def __init__(self, name, value, legs):
        super().__init__(name, value, legs)

    def decrease_hp(self):
        super().decrease_hp()

    def eat(self, food):
        if (isinstance(food, Grass) or isinstance(food, Animal)):
            Animal.eat(self, food)
        else:
            print(self.name + " cannot eat " + food.name)
            


def main():
    day = 0
    Map = {}
    for i in range(3):
        for j in range(2):
             Map[(i,j)] = Box(i, j)
    Map[(random.randint(0, 2), random.randint(0,1))].place(Animal("Chip", 15, 4))
    human = Omnivore("Justin", 50, 2)
    human.location = (0, 0)
    Map[(0, 0)].human = human
    Map[(0, 0)].water = WaterSource(200)
    Map[(random.randint(0, 2), random.randint(0,1))].grass = Grass(10)
    small_rock = Rock(5)
    while(True):
        day += 1
        print("Day " + str(day) + "...")
        human = daily_dose(human, day)
        if (human.hp <= 0): break
        spawn(Map)
        for _ in range(3):
            survival(human, Map)
        print("The next day... \n")

def water_level(Map, number):
    for i in Map:
        if (Map[i].water != []):
            Map[i].water.increase_water(number)
    
def spawn(Map):
    # Drought, Sunny Day, Drizzling, Rainy Day, Thunderstorm
    weather = random.randint(1, 18)
    if (weather <= 2): # Drizzle
        print("It's drizzling...")
        print("The river refilled a bit...")
        water_level(Map, 20)
    elif (weather <= 5): # Rain
        print("It's raining...")
        print("The river refilled some water...")
        water_level(Map, 40)
    elif (weather <= 6 or weather > 18): # Thunderstorm
        print("There is a thunderstorm!")
        print("The river floods...")
        water_level(Map, 80)
        if (random.randint(0, 1) == 1):
            try:
                food = Map[(random.randint(0, 1),random.randint(0, 2))].food
            except NameError:
                print("No one died from the thunderstorm...")
            else:
                print(food.pop(random.randint(0, len(food) - 1)).name + " died from the thunder storm... :(")           
    elif (weather <= 15): # Sunny Day
        print("It's a sunny day...")
    else: # Drought
        print("The weather is soooooo hot!")
        print("Some of the river dried up...")
        water_level(Map, -35)
        
    # Food
    animals = [("Chicken", random.randint(8,12), 2),
               ("Squirrel", random.randint(13,17), 4),
               ("Cow", random.randint(30,50), 4),
               ("Worm", random.randint(1,5), 0)]
    Map[random.randint(0, 2), random.randint(0, 1)].place(Animal(*animals[random.randint(0,3)]))
    Map[random.randint(0, 2), random.randint(0, 1)].place(Animal(*animals[random.randint(0,3)]))
    for i in Map:
        Map[i].move_all(Map)
        
def daily_dose(human, day):
    human.decrease_hp()
    if (human.hp <= 0):
        print(human.name + " died on Day " + str(day))
        return human
    human.increase_hunger()
    human.increase_thirst()
    return human

def survival(human, Map):
    map_print(Map)
    print("Current health: " + str(human.hp))
    print("Current hunger: " + str(human.hunger))
    print("Current thirst: " + str(human.thirst))
    print("Current location: " + str(human.location))
    action = input("What are you going to do? (Move/Eat/Drink)")
    action = action.lower()
    if (action != "eat" and action != "drink" and action != "move"):
        print("Invalid action!")
        survival(human, Map)
        
    elif (action == "move"):
        print("Where do you want to go?")
        print("1) Left \n2) Right\n3) Up\n4) Down")
        try:
            direction = int(input("Pick a number "))
        except ValueError:
            print("Invalid Option!")
            survival(human, Map)
        else:
            if (direction < 0 or direction > 4):
                print("Invalid Option!")
                survival(human, Map)
            else:
                temp = ()
                if (direction == 1):
                    temp = (max(0, human.location[0]-1), human.location[1])
                elif (direction == 2):
                    temp = (min(2, human.location[0]+1), human.location[1])
                elif (direction == 3):
                    temp = (human.location[0], min(1, human.location[1]+1))
                else:
                    temp = (human.location[0], max(0, human.location[1]-1))
                try:
                    if (temp == human.location):
                        raise MyError(direction)
                except MyError as e:
                    print(e)
                    survival(human, Map)
                else:
                    print("You moved")
                    Map[(human.location[0], human.location[1])].human = False
                    Map[temp].human = human
                    human.location = temp
    elif (action == "eat"):
        for i in range(len(Map[human.location].food)):
            print(str(i+1) + ") " + Map[human.location].food[i].name)
        choice = int(input("What would you like to eat? (Select a number)"))
        if (choice <= 0 or choice > len(Map[human.location].food)):
            print("Invalid Option!")
            survival(human, Map)
        else:
            human.eat(Map[human.location].food[choice - 1])
            print("You ate " + Map[human.location].food[choice - 1].name + " and you lost " + str(Map[human.location].food.pop(choice-1).value) + " hunger")
    else:
        if (Map[human.location].water != []):
            choice = int(input("How much would you like to drink? (1 to " + str(Map[human.location].water.amount) + ")"))
            if (choice < 1 or choice > Map[human.location].water.amount):
                print("Invalid Option")
                survival(human, Map)
            else:
                human.drink(Map[human.location].water, choice)
                print("You drank some water! Your thirst decreased by " + str(choice))


def map_print(Map):
    print(" --------" * 3)
    all_row = ["", "", "", ""]
    for i in range(0, 3):
        for j in range(4):
            if (j == 0 and Map[(i, 1)].human != False):
                all_row[j] += "|You     "
            elif (j == 3 and len(Map[(i, 1)].food) >= 3):
                  all_row[j] += "|+" + str(len(Map[(i, 1)].food) - 2) + " more"
            elif (j - (Map[(i, 1)].human != False) < len(Map[i, 1].food)):
                all_row[j] += "|" + Map[(i, 1)].food[j - (Map[(i, 1)].human != False)].name + " " * (8 - len(Map[(i, 1)].food[j - (Map[(i, 1)].human != False)].name))       
            else:
                all_row[j] += "|" + " " * 8
    for i in all_row: print(i + "|")
    
    print(" --------" * 3)
    
    all_row = ["", "", "", ""]
    for i in range(0, 3):
        for j in range(4):
            if (j == 0 and Map[(i, 0)].human != False):
                all_row[j] += "|You     "
            elif (j == 3 and len(Map[(i, 0)].food) >= 3):
                  all_row[j] += "|+" + str(len(Map[(i, 0)].food) - 2) + " more "
            elif (j - (Map[(i, 0)].human != False) < len(Map[i, 0].food)):
                all_row[j] += "|" + Map[(i, 0)].food[j - (Map[(i, 0)].human != False)].name + " " * (8 - len(Map[(i, 0)].food[j - (Map[(i, 0)].human != False)].name))       
            else:
                all_row[j] += "|" + " " * 8
    for i in all_row: print(i + "|")
    print(" --------" * 3)

    
class MyError(Exception):
    def __init__(self, direction):
        self.direction = direction
        print("MyError is working!")
    def __str__(self):
        return str(self.direction) + " is an invalid option!"
main()
