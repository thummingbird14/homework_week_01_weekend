# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dic):
    shop_name = pet_shop_dic["name"]
    return shop_name

def get_total_cash(pet_shop_dic):
    cash = pet_shop_dic["admin"]["total_cash"]
    return cash

def add_or_remove_cash(pet_shop_dic, cash_amount):
    pet_shop_dic["admin"]["total_cash"] += cash_amount

def get_pets_sold(pet_shop_dic):
    return pet_shop_dic["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_dic, addl_pets_sold):
    pet_shop_dic["admin"]["pets_sold"] += addl_pets_sold

def get_stock_count(pet_shop_dic):
    return len(pet_shop_dic["pets"])

def get_pets_by_breed(pet_shop_dic, breed_type):
    pets_in_breed = []
    for pet in pet_shop_dic["pets"]:
        if pet["breed"] == breed_type:
            pets_in_breed.append(pet)
    return pets_in_breed

def find_pet_by_name(pet_shop_dic, pet_name):
    for pet in pet_shop_dic["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop_dic, pet_name):
    # for pet in pet_shop_dic["pets"]:
        # if pet["name"] == pet_name:
            # del pet

    for i in range(len(pet_shop_dic["pets"])):
        if pet_shop_dic["pets"][i]["name"] == pet_name:
            del pet_shop_dic["pets"][i]
            break

def add_pet_to_stock(pet_shop_dic, new_pet_dic):
    pet_shop_dic["pets"].append(new_pet_dic)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_value):
    customer["cash"] -= cash_value

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet_dic):
    customer["pets"].append(new_pet_dic)

def customer_can_afford_pet(customer, new_pet_dic):
    if get_customer_cash(customer) >= new_pet_dic["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop_dic, pet_dic, customer):
    if pet_dic != None:
        if customer_can_afford_pet(customer, pet_dic):
            add_pet_to_customer(customer,pet_dic)
            pet_shop_dic["admin"]["pets_sold"]+=1
            cash_value = pet_dic["price"]
            remove_customer_cash(customer, cash_value)
            pet_shop_dic["admin"]["total_cash"] += cash_value
            remove_pet_by_name(pet_shop_dic,pet_dic["name"])

