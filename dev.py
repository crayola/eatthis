from eatthis.food import Meal, broccoli_gratin

meal = Meal([broccoli_gratin, broccoli_gratin])
print(meal.ingredients)

print(meal)
meal = meal.add(broccoli_gratin)
print(meal)
