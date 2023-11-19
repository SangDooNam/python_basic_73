from sort import Sort
from search import Search
from extraction import Extraction
from datetime import datetime
from loader import Loader


class AuthenticationError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


class Item:
    
    def __init__(self, state:str, category:str, warehouse:int, date_of_stock:datetime) -> None:
        self.state = state
        self.category = category
        warehouse = warehouse
        self.date_of_stock = datetime.strptime(date_of_stock, '%Y-%m-%d %H:%M:%S')
        
    def __str__(self) -> str:
        return self.state +' '+ self.category

class Stock:
    pass


class Warehouse:
    def __init__(self, warehouse_id:int) -> None:
        self.id = warehouse_id
        self.stock = []
    
    def occupancy(self) -> int:
        number_of_items = len(self.stock)
        return f'The number of items: {number_of_items}'
    
    
    def add_item(self, item:Item) -> None:
        self.stock.append(item)
    
    def search(self, search_term:str) -> list:
        self.sorted_list = Sort.heap(self.stock)
        self.search_item = Search.binary_search_range(self.sorted_list, search_term)
        self.result = Extraction.extraction(self.sorted_list, self.search_item)
        return self.result


class User:
    
    def __init__(self, user_name:str) -> None:
        self._name = user_name if user_name else 'Anonymous'
        self.is_authenticated = False

    
    def authenticate(self, password:str) -> False:
        return False
    
    
    def is_named(self, name:str) -> bool:
        return self._name == name
        
    
    def greet(self) -> None:
        print(f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you.")

    
    def bye(self, actions:list = None) -> None:
        print(f"Thank you for your visit, {self._name}!")

    
class Employee(User):
    
    def __init__(self, user_name: str, password:str, head_of: list = None) -> None:
        super().__init__(user_name)
        self.__password = password
        self.head_of = [Employee(**member) for member in head_of] if head_of else []
    
    def authenticate(self, password: str) -> bool:
        self.password = password
        if self.__password == password:
            self.is_authenticated = True
            return True
        else:
            raise AuthenticationError('Password is incorrect.')
        
    def order(self, item:Item, amount:int) -> None:
        print(f'Ordered {amount} of {item}.')
        
    def greet(self) -> None:
        print(f'Hello {self._name}!\nIf you experience a problem with the system,\nplease contact technical support.')
    
    def bye(self, actions: list) -> None:
        super().bye()
        if actions:
            print('Actions taken during the session:')
            for action in actions:
                print(action)

