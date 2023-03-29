from data4 import personnel, stock
import time
from datetime import datetime

from methods_moita_W4 import get_user_name, greet_user, get_selected_operation
from methods_moita_W4 import ordering, list_items_by_warehouse, search_and_order_item
from methods_moita_W4 import browse_by_category, invalid_operation
from methods_moita_W4 import extracted_user_password, autorizado


user_name = get_user_name()
greet_user(user_name)

new_personnel = extracted_user_password(personnel)
for i in new_personnel:
    print(i)
print()

operation = get_selected_operation()


while True:
    if operation == 1:
        list_items_by_warehouse()

    elif operation == 2:
        search_and_order_item()

    elif operation == 3:
        browse_by_category()

    elif operation == 4:
        print('\nThank for visiting us')
        break

    else:
        invalid_operation()

    operation = get_selected_operation()
