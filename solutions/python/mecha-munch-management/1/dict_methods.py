"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    updated_cart = current_cart.copy()
    for item in items_to_add:
            if item in updated_cart:
                updated_cart[item] += 1
            else:
                updated_cart[item] = 1
    return updated_cart



def read_notes(notes):
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart



def update_recipes(ideas, recipe_updates):
    for recipe_name, new_ingredients in recipe_updates:
        ideas[recipe_name] = new_ingredients
    return ideas


def sort_entries(cart):
    return {key: cart[key] for key in sorted(cart)}


def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}
    for item in sorted(cart.keys(), reverse=True):
        quantity = cart[item]
        aisle, refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]
    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, order_info in fulfillment_cart.items():
        if item in store_inventory:
            current_stock = store_inventory[item][0]
            order_quantity = order_info[0]
            new_stock = current_stock - order_quantity
            if new_stock <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_stock
    return store_inventory
