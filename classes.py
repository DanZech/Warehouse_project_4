from datetime import datetime


class Warehouse():
    def __init__(self,  warehouse_id, int = None):
        self.id = warehouse_id
        self.stock = []
        self.item = Item()
        # does not require stock argument because stock will ...

    def occupancy(self):
        return len(self.stock) #return an integer representing 

    def add_item(self, item): # take instance of item as an argument, add the given object to the stock property
        self.stock.append(item) 

    def search(self, search_term):
        #search the items in teh current warehouse and will return the list
        #of the matching items according to the ...

        #encontrou_item = []
        #for item in self.stock:
        #    if search_term in item.state or search_term in item.category:
        #        encontrou_item.append(item)
        #return encontrou_item
        pass

    def listItems(self):
        pass

    def __str__(self):
        return f'Warehouses: {self.id}'


class Item:
    # the items will be stored in the 'stock' property of each 'warehouse' object,  
    # so the item does not need this
    def __init__(self, state: str = None, category: str = None, date_of_stock: datetime = None, warehouse: int = 1):
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    # this method should return the concatenation of the properties 'state' and 'category'
    def __str__(self) -> str:
        item = self.state + ' ' + self.category
        return f'Item: {self.category}'


class User():
    def __init__(self, user_name: str='Anonymous'):
        self.name = user_name
        self.is_authenticated = False           #employee or guest

        def authenticate(self):
            return False                    # placeholder for feature
        
        def greet(self):
            return f'Hello, {self._name}!\n\
                Welcome to our Warehouse Database.\n\
                If you dont\'find waht you are looking for ...'
        
        def is_named(self, name):
            if name == self.name:
                return True
            return False

        def bye(self):
            print(f'Thank you for your visit, {self._name}!')
            # guest user will nopt be show the summary of its actions
        

class Employee(User): 
    def __init__(self, user_name, password, head_of = []):
        super().__init__(user_name)
        self.__password = password
        self.head_of = head_of
    
    def authenticate(self, password):
        if self.__password == password:          # return true if the argument password matches the property __password
            return True
        return False
    
    def order(self, item, amount: int):
        print(f'Item: {item}\nAmount: {amount}')

    def greet(self):
        print(f'Hello, {User._name}!n\
              If you experienced a problem with the systen,\n\
              please contact our technical support.')

    def bye(self):
        super().bye

        