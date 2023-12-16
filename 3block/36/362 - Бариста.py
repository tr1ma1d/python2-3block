def choose_coffee(*preference):
    for coffee in preference:
        if ('Эспрессо' == coffee) and (ingredients[0] >= 1):
            ingredients[0] -= 1
            return 'Эспрессо'
        elif ('Капучино' == coffee) and (ingredients[0] >= 1 and ingredients[1] >= 3):
            ingredients[0] -= 1
            ingredients[1] -= 3
            return 'Капучино'
        elif ('Маккиато' == coffee) and (ingredients[0] >= 2 and ingredients[1] >= 1):
            ingredients[0] -= 2
            ingredients[1] -= 1
            return 'Маккиато'
        elif ('Кофе по-венски' == coffee) and (ingredients[0] >= 1 and ingredients[2] >= 2):
            ingredients[0] -= 1
            ingredients[2] -= 2
            return 'Кофе по-венски'
        elif ('Латте Маккиато' == coffee) and (ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1):
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
            return 'Латте Маккиато'
        elif ('Кон Панна' == coffee) and (ingredients[0] >= 1 and ingredients[2] >= 1):
            ingredients[0] -= 1
            ingredients[2] -= 1
            return 'Кон Панна'
    return 'К сожалению, не можем предложить Вам напиток'


ingredients = [1, 2, 3]
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))


