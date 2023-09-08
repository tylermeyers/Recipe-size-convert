from collections import deque
import math
#recipe sizes converter

# 2 options :(1) Based off of entired recipe (ie only want half the portions)
#         -- (2)Based off a  single dish (only have x amount of dish)
class Ingredient:
    class parsed_size:
        def __init__(self, in_size) -> None:
            num = ''
            unit = ''

            for i in in_size:
                if(i.isdigit()):
                    num = num+i
                else:
                    unit = unit+i

            self.num = int(num)
            self.unit = unit

        def get_parse(self) -> str:
            return str(self.num) + " " + self.unit

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = Ingredient.parsed_size(size)

    def in_print(self) -> None:
        print(self.name +": " +self.size.get_parse())



#ingredient1.in_print()

#Initializing important var's
q = deque()
num_ingre = int(input("How many ingredients are there in your recipe? ").strip())
conversion_size = float(input("By how much do you want convert the recipe(ie .5, 1.5): "))



#Collecting all ingredients + the size
for i in range(num_ingre):
    ingredient = Ingredient(input("Ingredient name: ").strip(), input("Amount: ").strip())
    ingredient.size.num = ingredient.size.num*conversion_size
    q.append(ingredient)

while(bool(q)):
    Ingredient.in_print(q.popleft())





