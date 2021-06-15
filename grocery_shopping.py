prices = {'Apple': 5, 'Banana': 2, 'Orange': 3, 'Lemon': 1, 'Grapefruit': 8}
shopping_cart = {}

while input('Enter to stop, else press any key then Enter'):
    prod = input('Product: ')
    if prod not in prices.keys():
        print('{0} does not exist.'.format(prod))
        continue
    amount = int(input('Amount: '))
    try:
        shopping_cart[prod] = amount
    except Exception:
        pass

total = sum(shopping_cart.values())

print(total)
