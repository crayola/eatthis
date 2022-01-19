from dataclasses import dataclass
import random

@dataclass(eq=True, unsafe_hash=True)
class Ingredient():
    name: str
    season: tuple[int]
    nutrition: tuple[int]

    def __post_init__(self):
        self.has_fiber = True if self.nutrition[0] else False
        self.has_carbs = True if self.nutrition[1] else False
        self.has_proteins = True if self.nutrition[2] else False


@dataclass
class Dish():
    name: str
    ingredients: list[Ingredient]
    course: int

    def __post_init__(self):
        self.has_fiber = True if any([x.has_fiber for x in self.ingredients]) else False
        self.has_carbs = True if any([x.has_carbs for x in self.ingredients]) else False
        self.has_proteins = True if any([x.has_proteins for x in self.ingredients]) else False

@dataclass
class Meal():
    dishes: list[Dish]

    def __post_init__(self):
        self.has_fiber = True if any([x.has_fiber for x in self.dishes]) else False
        self.has_carbs = True if any([x.has_carbs for x in self.dishes]) else False
        self.has_proteins = True if any([x.has_proteins for x in self.dishes]) else False
        self.ingredients = set([i for d in self.dishes for i in d.ingredients])
    
    def add(self, dish):
        return Meal(self.dishes + [dish])


broccoli = Ingredient(
    name = "Broccoli",
    season = (1,) * 12,
    nutrition = (1, 0, 0)
    )

cheese = Ingredient(
    name = "Cheese",
    season = (1,) * 12,
    nutrition = (0, 0, 1)
)

broccoli_gratin = Dish(
    name = "Broccoli Gratin",
    ingredients = [broccoli, cheese],
    course = 1
)

# dish_menu = 

sample_line = "ratatouille,7,60,5,4,1111,101"

def parse_dish(line):
    dish_list = line.split(',')
    return Dish(dish_list[0], [], [])

def is_balanced(meal: Meal):
    return meal.has_carbs and meal.has_fiber and meal.has_proteins

def compose_meal(dish_menu: list[Dish]):
    meal = Meal(random.choice(dish_menu))
    meal2 = meal
    
    while not(is_balanced(meal2)):
        meal2 = meal.add(random.choice(dish_menu))
        
    return meal2
    
    

