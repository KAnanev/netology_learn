cook_book = {}
with open('recipes.txt') as f:
    list_dishes = f.read()
    list_dishes = list_dishes.split('\n\n')
    list_dishes = [dish.split('\n') for dish in list_dishes]
    for i in list_dishes:
        i[1:] = [i[2:]]
        i[1] = [dish.split('|') for dish in i[1]]
        i[1] = [dict(zip(['ingredient_name', 'quantity', 'measure'], i)) for i in i[1]]
    cook_book = dict(list_dishes)


def get_shop_list_by_dishes(dishes, person_count):
    temp_list1 = []
    temp_list2 = []
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for item in ingredients:
                item['quantity'] = int(item['quantity']) * person_count
                temp_list1.append(item['ingredient_name'])
                del item['ingredient_name']
                temp_list2.append(item)
    dict_ingredients = dict(zip(temp_list1, temp_list2))
    print(dict_ingredients)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
