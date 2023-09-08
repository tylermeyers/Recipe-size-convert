from collections import deque
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


q = deque()

if(int(input("Option: 0 (conversion based off ingredient) or option 1 (conversion based off entire recipe?)"))):
    conversion_size = float(input("By how much do you want convert the recipe(ie .5, 1.5): "))
else:
    ingredient_name = input("Ingredient name: ").strip()
    amount = input("Amount you have: ").strip()
    ingredient = Ingredient(ingredient_name, amount )

    conversion_size = ingredient.size.num/Ingredient.parsed_size(input("Amount in recipe: ").strip()).num
    q.append(ingredient)
    print("DONT RE-ENTER INGREDIENT AND DO NOT INCLUDE IN NEXT QUESTION")


num_ingre = int(input("How many ingredients are there in your recipe? ").strip())


#Collecting all ingredients + the size
for i in range(num_ingre):
    ingredient = Ingredient(input("Ingredient name: ").strip(), input("Amount: ").strip())
    ingredient.size.num = ingredient.size.num*conversion_size
    q.append(ingredient)

print("Ingredients: ")
while(bool(q)):
    Ingredient.in_print(q.popleft())