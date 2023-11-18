from sort import Sort
from search import Search
from extraction import Extraction
from datetime import datetime

class Item:
    
    def __init__(self, state:str, category:str, warehouse:int, date_of_stock:datetime) -> None:
        self.state = state
        self.category = category
        warehouse = warehouse
        self.date_of_stock = date_of_stock
        
    def __str__(self,) -> str:
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


class personnel:
    pass



a = Warehouse(10)

print(a.search('Donec'))