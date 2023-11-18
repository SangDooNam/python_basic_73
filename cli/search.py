

class Search:
    
    @staticmethod
    def first(arr, search_term):
        
        left = 0
        right = len(arr) - 1
        result = -1
        
        while right >= left:

            middle = (left + right) // 2
            
            if arr[middle] == search_term:
                result = middle
                right = middle - 1
            elif arr[middle] < search_term:
                left = middle + 1
            else:
                right = middle - 1
                
        return result
    
    @staticmethod
    def last(arr, search_term):
        
        left = 0
        right = len(arr) - 1
        result = -1
        
        while right >= left:
            
            middle = (left + right) // 2
            
            if arr[middle] == search_term:
                result = middle
                left = middle + 1
                
            elif arr[middle] < search_term:
                left = middle + 1
            else:
                right = middle - 1
        
        return result
    
    @staticmethod
    def binary_search_range(arr, search_term):
        
        return Search.first(arr, search_term), Search.last(arr, search_term)

