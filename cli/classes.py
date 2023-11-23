from datetime import datetime


class Item:
    
    def __init__(self, state:str, category:str, warehouse:int, date_of_stock:datetime) -> None:
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock
        
    def __str__(self) -> str:
        
        return f'{self.state} {self.category}'


class Warehouse:
    
    def __init__(self, warehouse_id:int) -> None:
        self.id = warehouse_id
        self.stock = []
    
    def occupancy(self) -> int:
        
        return len(self.stock)
    
    
    def add_item(self, item:Item) -> None:
        self.stock.append(item)
        
    def search(self, search_term: str) -> list:
        
        return [item for item in self.stock if search_term == item.state + ' ' + item.category or search_term == item.date_of_stock]

class User:
    
    def __init__(self, user_name:str) -> None:
        self._name = user_name if user_name else "Anonymous"
        self.is_authenticated = False
        
    
    def authenticate(self, password:str) -> False:
        
        return False
    
    def is_named(self, name:str) -> bool:
        return self._name == name
        
    
    def greet(self) -> None:
        print(f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you.")

    def bye(self, actions:list) -> None:
        print(f'Thank you, {self._name}')


class Employee(User):
    
    def __init__(self, user_name: str, password:str, head_of:list=None) -> None:
        super().__init__(user_name)
        self.user_name = user_name
        self.__password = password
        self.head_of = [Employee(**employee) for employee in head_of] if head_of else []
    
    def authenticate(self, password: str) -> bool:
        if self.__password == password:
            self.is_authenticated = True
            return True
        else:
            return False
    
    def order(self, item:Item, amount:int) -> None:
        print(f'Ordered {amount} of {item} ')
        
    def greet(self) -> None:
        print(f'Hello, {self._name}!\nIf you experience a problem with the system,\nplease cantact technical support')
    
    def bye(self, actions: list) -> None:
        super().bye(actions)
        if actions:
            for action in actions:
                print(action)
    
    def __str__(self) -> str:
        return f'{self.user_name}, {self.head_of}'