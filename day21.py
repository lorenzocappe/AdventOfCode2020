def read_file() -> list:
    line_list = []

    file = open("input21.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


class Food:
    def __init__(self, text: str, number: int):
        self.ingredient_list = set()
        self.allergen_list = set()

        temp = text.split(' (contains ')

        for ingredient in temp[0].split(' '):
            self.ingredient_list.add(ingredient)

        for allergen in temp[1][:-1].split(', '):
            self.allergen_list.add(allergen)

        self.id = number
        return

    def __str__(self):
        return '{'+str(self.ingredient_list)+', '+str(self.allergen_list)+'}'

    def __repr__(self):
        return '{'+str(self.id)+'}'


def create_food_list(input_lines: list) -> list:
    result = []
    for index in range(len(input_lines)):
        result.append(Food(input_lines[index], index))

    return result


def create_full_ingredient_list(food_list: list) -> dict:
    result = dict()
    for food in food_list:
        for ingredient in food.ingredient_list:
            if ingredient not in result:
                result[ingredient] = 0
            result[ingredient] += 1

    return result


def find_ingredients_containing_allergens(food_list: list) -> dict:
    result = dict()
    considered_allergens = set()

    for food in food_list:
        for allergen in food.allergen_list:
            if allergen not in considered_allergens:
                temp = food.ingredient_list.copy()
                for other_food in food_list:
                    if allergen in other_food.allergen_list:
                        temp.intersection_update(other_food.ingredient_list.copy())

                result[allergen] = temp
                considered_allergens.add(allergen)

    return result


def create_suspect_ingredient_list(food_list: list) -> set:
    result = set()

    temp = find_ingredients_containing_allergens(food_list)
    for allergen in temp:
        for ingredient in temp[allergen]:
            result.add(ingredient)

    return result


def create_clear_ingredient_list(full_ingredients: dict, suspect_ingredients: set) -> dict:
    clear_ingredients = full_ingredients.copy()
    for ingredient in suspect_ingredients:
        clear_ingredients.pop(ingredient)

    return clear_ingredients


def find_number_clear_ingredients(clear_ingredients: dict) -> int:
    result = 0
    for ingredient in clear_ingredients:
        result += clear_ingredients[ingredient]

    return result


def find_allergen_for_ingredient(food_list: list) -> dict:
    ingredients_for_allergen = find_ingredients_containing_allergens(food_list)
    allergen_list = list(ingredients_for_allergen.keys())

    result = dict()
    while len(allergen_list) > 0:
        temp = allergen_list.pop()
        if len(ingredients_for_allergen[temp]) > 1:
            allergen_list.insert(0, temp)
        else:
            result[temp] = ingredients_for_allergen[temp].pop()
            ingredients_for_allergen.pop(temp)
            for allergen in allergen_list:
                if result[temp] in ingredients_for_allergen[allergen]:
                    ingredients_for_allergen[allergen].remove(result[temp])

    return result


def main():
    input_lines = read_file()
    # print(input_lines)

    food_list = create_food_list(input_lines)
    # for food in food_list:
    #     print(food)

    full_ingredient_list = create_full_ingredient_list(food_list)
    # print(full_ingredient_list)

    suspect_ingredient_list = create_suspect_ingredient_list(food_list)
    # print(suspect_ingredient_list)

    clear_ingredient_list = create_clear_ingredient_list(full_ingredient_list, suspect_ingredient_list)
    # print(clear_ingredient_list)

    # print(find_ingredients_containing_allergens(food_list))
    print(find_number_clear_ingredients(clear_ingredient_list))

    allergen_for_ingredient_list = find_allergen_for_ingredient(food_list)
    # print(allergen_for_ingredient_list)

    result = ''
    temp = list(allergen_for_ingredient_list.keys())
    temp.sort()
    for allergen in temp:
        result += allergen_for_ingredient_list[allergen] + ','
    print(result[:-1])


if __name__ == '__main__':
    main()
