from data4 import stock, personnel
import time
from datetime import datetime

warehouse1, warehouse2, warehouse3, warehouse4 = [], [], [], []
founded_items = 0
search_item = 0
user_name = ""


def get_user_name():
    username = input('Username: ')
    return username

def greet_user(user_name):
    print(f'\nHello {user_name}\n\n')

#----------------------------------------------------------------------------
def extracted_user_password(the_fucking_dicts):
    result = list()
    for user_in_dict in the_fucking_dicts:
        new_dict = {}
        new_dict["user_name"] = user_in_dict["user_name"]
        new_dict["password"] = user_in_dict["password"]
        result.append(new_dict)
        if "head_of" in user_in_dict:
            result.extend(extracted_user_password(user_in_dict["head_of"]))
    return result

new_personnel = extracted_user_password(personnel)

#-----------------------------------------------------------------------

def autorizado():
    new_personnel = extracted_user_password(personnel)

    for dicts in new_personnel:
        if user_name not in dicts['user_name']:
            raise ValueError('ALERTA DE INTRUSO!')
        elif user_name in dicts['user_name']:
            senha = input('Digite a senha: ')
            if senha not in dicts['password']:
                raise ValueError('ERRADO!')
            elif senha in dicts['password']:
                print('Senha autorizada!!!')
                return True

#=========================================================================

def get_selected_operation():
    operation = int(input('Choose an option:\n\
      1. List items by warehouse;\n\
      2. Search an item and place an order;\n\
      3. Browse by category\n\
      4. Quit;\n\
        Enter your choise: '))
    return operation


def list_items_by_warehouse():
    counter_all = 0
    counter_w1 = 0
    counter_w2 = 0
    counter_w3 = 0
    counter_w4 = 0
    # print('\nItems from warehouse 1: \n')
    for i1 in stock:
        if i1["warehouse"] == 1:
            counter_all += 1
            counter_w1 += 1
            ware_1 = i1["state"].lower() + ' '+i1["category"].lower()
            warehouse1.append(ware_1)

    for i2 in stock:
        if i2["warehouse"] == 2:
            counter_all += 1
            counter_w2 += 1
            ware_2 = i2["state"].lower() + ' '+i2["category"].lower()
            warehouse2.append(ware_2)

    for i3 in stock:
        if i3["warehouse"] == 3:
            counter_all += 1
            counter_w3 += 1
            ware_3 = i3["state"].lower() + ' '+i3["category"].lower()
            warehouse3.append(ware_3)

    for i4 in stock:
        if i4["warehouse"] == 4:
            counter_all += 1
            counter_w4 += 1
            ware_4 = i4["state"].lower() + ' '+i4["category"].lower()
            warehouse4.append(ware_4)

    combined = list(zip(warehouse1, warehouse2, warehouse3, warehouse4))
    # find the maximum length of any item in either list
    max_len = max(max(len(x) for x in warehouse1), max(len(x)
                                                       for x in warehouse2), max(len(x) for x in warehouse3), max(len(x) for x in warehouse4))

    # print the items side by side
    cu = 0
    cu4 = 0
    print('\nWe have in stock the following items:\n')
    for item1, item2, item3, item4 in combined:
        cu = cu4
        item1 = item1.ljust(max_len)
        cu1 = cu + 1
        item2 = item2.ljust(max_len)
        cu2 = cu1 + 1
        item3 = item3.ljust(max_len)
        cu3 = cu2 + 1
        item4 = item4.ljust(max_len)
        cu4 = cu3 + 1

        print(f"{cu1}.{item1}   {cu2}.{item2}   {cu3}.{item3}   {cu4}.{item4}")
        # time.sleep(0.05)

    print(f'\nTotal itens in warehouse 1: {counter_w1}')
    print(f'Total itens in warehouse 2: {counter_w2}')
    print(f'Total itens in warehouse 2: {counter_w3}')
    print(f'Total itens in warehouse 2: {counter_w4}')

    print(
        f'Total items in stock: {counter_w1 + counter_w2 + counter_w3 + counter_w4}\n')
    #print(f'Here is a test if another variable: {counter_all}')


def search_and_order_item():
    counter3 = 0
    search_item = input('\nWhat is the item name: ').lower()
    print()
    found = dict()
    founded_items = list()

    for i in stock:
        produto = i["state"].lower() + ' '+i["category"].lower()
        if search_item == produto:
            counter3 += 1
            found.update(
                {'item': produto, 'warehouse': i['warehouse'], 'date': i['date_of_stock']})
            founded_items.append(found)

            for d in founded_items:
                now = datetime.now()
                data_convertida = datetime.strptime(
                    d['date'], "%Y-%m-%d %H:%M:%S")
                how_long = now - data_convertida

            print(f"- Warehouse {found['warehouse']} (in stock for {how_long.days} days)")

    print(f'\nTotal of "{search_item}" in stock: {len(founded_items)}')

    ordering(founded_items)
    

def ordering(founded_items):
    order = input('\nWould you like to order this item?(y/n) ')

    if order == 'y':
        
        try:
            autorizado()

            qtde = int(input('How many would you like to order? '))

            if qtde <= len(founded_items):
                print('Thank you very much for your preference buying with us.')
                
            elif qtde > len(founded_items):
                print(f'\n\
                    **************************************************\n\
                    There are not this many available.\n\
                    The maximum amount that can be ordered is {len(founded_items)}\n\
                    **************************************************\n')
                order = input(
                    f'Would like to order all {len(founded_items)} items we have in stock? (y/n) ')
                if order == 'y':
                    print(
                        f'Thank you very much for buying our all {len(founded_items)} {search_item}.')
                elif order == 'n':
                    qtde = int(input(
                        f'Inform the amout of {search_item} less/equal than {len(founded_items)} that you would like to order: '))
                    print(f'Thank you for ordening {qtde} {search_item} with us.')
            elif order == 'n':
                pass
        
        except ValueError as e:
            print(str(e))


def browse_by_category():
    from prettytable import PrettyTable
    categories = list()
    contagem_items = dict()
    counter4 = 0

    for i in stock:
        categories.append(i['category'])
    # print(categories)

    for item in categories:
        if item not in contagem_items:
            contagem_items[item] = 0
        contagem_items[item] += 1
    # print(contagem_items)

    tabela = PrettyTable(['N°', 'Daniel', 'Qty'])
    item_linha = dict()
    # *args & **kwargs 


    for k, v in contagem_items.items():
        counter4 += 1
        tabela.add_row([counter4, k, v])
        item_linha[counter4] = (k, v)
    print(tabela)

    selection = int(input('\nType the number of the category to browse: '))
    if selection in item_linha:
        category, qty = item_linha[selection]
        print(
            f"You selected '{category}' with {qty} items.\n")

        counter5 = 0
        for c in stock:
            if category == c['category']:
                counter5 += 1
                ste_cat = c['state'].lower() + ' '+c['category']
                print(f'{counter5}. {ste_cat}')

    else:
        print("Invalid number. Try again.")
        pass

  
def invalid_operation():
    print('*'*50)
    print("\nInvalid data. Try again.")
    print('*'*50)
    pass
