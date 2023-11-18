from search import Search

class Extraction:
    
    @staticmethod
    def extraction(arr:list, tuple:tuple, result=[]) -> list:
        left = tuple[0]
        right = tuple[1]
        
        while left <= right:
            result.append(arr[left])
            left += 1
        
        return result
    
    
