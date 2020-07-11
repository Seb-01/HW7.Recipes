
# D:\Documents\Нетология. Курс Python\HW.7.Recipe\recipes.txt
from pprint import pprint

def get_cook_book(file_name) -> dict:
    """
    Считываем книгу рецептов из файла на диске:
    :param file_name:
    :return:
    """
    # создаем словарь
    #cook_book=dict()
    recipes=dict()

    #открываем файл
    with open(file_name, 'rt', encoding='utf-8') as cook_book:
        while cook_book:
            # сохраняем блюдо в словарь (пробелы и символ картеки не забываем убирать!)
            name = cook_book.readline().rstrip('\n')
            num_ingrediens = int(cook_book.readline())
            list_ingreds=[]

            for i in range(num_ingrediens):
                dict_ingred = dict()
                list_ingred=cook_book.readline().split('|')
                dict_ingred['ingredient_name']=list_ingred[0].strip()
                dict_ingred['quantity'] = int(list_ingred[1])
                dict_ingred['measure'] = list_ingred[2].strip()
                list_ingreds.append(dict_ingred)
            recipes[name]=list_ingreds
            blank=cook_book.readline() # пустая строка между записями
            if blank=='': # конец файла
                break

    #pprint(recipes)
    #печать списка блюд
    #print(list(recipes.keys()))
    return recipes


def get_shop_list_by_dishes(order, recipes) -> dict:
    """
    получаем список ингредиентов и их количество для покупки и приготовления блюд из полученного заказа
    :param dishes_list:
    :param person_quantity:
    :return dict(ingredients):
    """

    ingredients=dict()
    # идем по списку заказа
    for dish in order:
        # добавляем ингредиенты блюда в список покупок
        for ingred in recipes[dish]:
            # если ингредиент уже есть в списке покупок - добавляем количество
            if ingred['ingredient_name'] in ingredients.keys():
                ingredients[ingred['ingredient_name']]['quantity'] += (order[dish] * ingred['quantity'])
            # если нет - добавляем ингредиент в список покупок
            else:
                ingredients[ingred['ingredient_name']]={'measure': ingred['measure'], 'quantity': ingred['quantity'] * order[dish]}

    return ingredients


def main():
    file_name=input('Укажите полное имя файла с рецептами: ')
    # считываем книгу с рецептами
    recipes=get_cook_book(file_name)
    # получаем блюда
    dishes=list(recipes.keys())
    # получаем заказ из блюд:
    order=dict()
    for dish in dishes:
        order[dish]=int(input(f'На сколько персон приготовить {dish}? - '))

    # заказ
    print(f'\nВаш заказ:\n{order}')

    # список покупок формируем
    shop_list=get_shop_list_by_dishes(order, recipes)
    print('Ваш список покупок:')
    pprint(shop_list)


if __name__ == '__main__':
    main()
