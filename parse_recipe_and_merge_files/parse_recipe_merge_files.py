import os


def parse_ingredients(file, ingredients_count):
    ingredients = []
    for _ in range(ingredients_count):
        line = file.readline().strip()
        ingredient_name, quantity, measure = line.split(" | ")
        ingredients.append({
            "ingredient_name": ingredient_name.strip(),
            "quantity": int(quantity),
            "measure": measure.strip()
        })
    return ingredients


def parse_recipe(file_path):
    with open(file_path, encoding="utf-8") as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            cook_book[dish_name] = parse_ingredients(file, ingredients_count)
            file.readline()  # Skip empty line between dishes
    return cook_book


def get_shop_list_by_dishes(dishes, person):
    try:
        recipes = parse_recipe("recipes.txt")
    except FileNotFoundError:
        print("Error: File 'recipes.txt' not found")
        return {}
    except Exception as err:
        print(f"Error reading file 'recipes.txt': {err}")
        return {}
    shop_list = {}
    for dish in dishes:
        try:
            if dish not in recipes:
                raise KeyError(f"The '{dish}' is not included in the recipes.")
            ingredients = recipes[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient["ingredient_name"]
                if ingredient_name in shop_list:
                    required_amount = ingredient["quantity"] * person
                    shop_list[ingredient_name]["quantity"] += required_amount
                else:
                    shop_list[ingredient_name] = {
                        "measure": ingredient["measure"],
                        "quantity": ingredient["quantity"] * person
                    }
        except KeyError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Unexpected error occured: {err}")
    return shop_list


def merge_files(folder=r".\\to_sort", result_file="result_merge_file.txt"):
    files_list = []
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                file_lines = file.readlines()
                num_lines = len(file_lines)
                files_list.append((file_name, num_lines, file_lines))
    files_list.sort(key=lambda x: x[1])
    with open(result_file, "w", encoding="utf-8") as file:
        for file_name, num_lines, file_lines in files_list:
            file.write(f"{file_name}\n")
            file.write(f"{num_lines}\n")
            file.writelines(file_lines)


if __name__ == "__main__":
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 4))
    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
    merge_files()
