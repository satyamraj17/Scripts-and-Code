from collections import defaultdict
from sortedcontainers import SortedSet

class FoodRating:

    def __init__(self, foods, cuisine, ratings):
        self.food_rating = dict()
        self.food_cuisine = dict()
        self.cuisine_food = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.food_rating[foods[i]] = ratings[i]
            self.food_cuisine[foods[i]] = cuisine[i]
            self.cuisine_food[cuisine[i]].add((-1*ratings[i], foods[i]))
        
    def change_rating(self, food, new_rating):
        cuisine_name = self.food_cuisine[food]
        old_food_rating = (-self.food_rating[food], food)
        self.cuisine_food[cuisine_name].remove(old_food_rating)
        self.food_rating[food] = new_rating
        self.cuisine_food[cuisine_name].add((-new_rating, food))
    
    def highest_rated(self, cuisine):
        return self.cuisine_food[cuisine][0][1]

foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisine = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
rating = [9, 12, 8, 15, 14, 7]

obj1 = FoodRating(foods, cuisine, rating)

print(obj1.highest_rated("korean"))
print(obj1.highest_rated("japanese"))
print(obj1.change_rating("sushi", 16))
print(obj1.highest_rated("japanese"))
print(obj1.change_rating("ramen", 16))
print(obj1.highest_rated("japanese"))
