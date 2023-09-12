from collections import deque
#recipe sizes converter


class Ingredient:
    """
    Ingredient class
    """

    class parsed_size:

        """
        parsed_size class
        """

        def __init__(self, in_size) -> None:
            """
            Constructor that parses float/int from size input

            @param in_size: User input for ingredient size (may include unit of measure)
            """
            num = ''
            unit = ''
            for i in in_size:
                if(i.isdigit() or i == '.'):
                    num = num+i
                else:
                    unit = unit+i

            self.num = float(num)
            self.unit = unit

        def __str__(self) -> str:
            return str(self.num) + " " + self.unit
        """
        String representation of the parsed_size object
        """
    def __init__(self, name, size) -> None:
        """
        Constructor for Ingredient class, size parsed via nested class

        @param name: User inputted name of ingredient
        @param size: User inputted size of ingredient
        """
        self.name = name
        self.size = Ingredient.parsed_size(size)

    def print(self) -> None:
        """
        Overloaded print statement for Ingredient class
        """
        print(self.name +": " +str(self.size))



#initializing deque for use in printing out converted recipe

q = deque()


#Option selection
if (int(input("Option: 0 (conversion based off ingredient) or option 1 (conversion based off entire recipe?)"))):
    conversion_size = float(input("By how much do you want convert the recipe(ie .5, 1.5): "))
else:
    ingredient_name = input("Ingredient name: ").strip()
    amount = input("Amount you have: ").strip()
    ingredient = Ingredient(ingredient_name, amount )

    conversion_size = ingredient.size.num/Ingredient.parsed_size(input("Amount in recipe: ").strip()).num
    q.append(ingredient)
    print("DONT RE-ENTER INGREDIENT AND DO NOT INCLUDE IN NEXT QUESTION")

#Collecting all ingredients + the size
num_ingre = int(input("How many ingredients are there in your recipe? ").strip())
for i in range(num_ingre):
    ingredient = Ingredient(input("Ingredient name: ").strip(), input("Amount: ").strip())
    ingredient.size.num = ingredient.size.num*conversion_size
    q.append(ingredient)

#print converted recipe
print("Ingredients: ")
while(bool(q)):
    Ingredient.print(q.popleft())