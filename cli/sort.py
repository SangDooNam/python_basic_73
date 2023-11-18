
class Sort:
    @staticmethod
    def heapify(arr, len_arr, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len_arr and arr[largest] < arr[left]:
            largest = left
        if right < len_arr and arr[largest] < arr[right]:
            largest = right
        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            Sort.heapify(arr, len_arr, largest)

    @staticmethod
    def heap(arr):
        len_arr = len(arr)

        for index in range(len_arr // 2 - 1, -1, -1):
            Sort.heapify(arr, len_arr, index)

        for index in range(len_arr - 1, 0, -1):
            arr[index], arr[0] = arr[0], arr[index]
            Sort.heapify(arr, index, 0)

        return arr
    
    @staticmethod
    def merge_sort2(arr, left=0, right=-1):
        if right == -1:
            right = len(arr) - 1
        
        if right > left:
            middle = (right + left) // 2
            Sort.merge_sort2(arr, left, middle)
            Sort.merge_sort2(arr, middle+1, right)
            return Sort.merge2(arr, left, middle, right)
            
    @staticmethod
    def merge2(arr, left, middle, right):
        
        len_left = middle - left + 1
        len_right = right - middle
        
        left_lst = [None] * len_left
        right_lst = [None] * len_right
        
        for i in range(len_left):
            left_lst[i] = arr[left + i]
        
        for j in range(len_right):
            right_lst[j] = arr[middle + 1 + j]
            
        i = 0
        j = 0
        k = left
        
        while i < len_left and j < len_right:
            if left_lst[i] < right_lst[j]:
                arr[k] = left_lst[i]
                i += 1
            else:
                arr[k] = right_lst[j]
                j += 1
            k += 1
        
        while i < len_left:
            arr[k] = left_lst[i]
            i += 1
            k += 1
        while j < len_right:
            arr[k] = right_lst[j]
            j += 1
            k += 1
            
        return arr
        
    @staticmethod
    def merge_sort(arr):
        
        if len(arr) <= 1:
            return arr
        
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        
        left_lst = Sort.merge_sort(left)
        right_lst = Sort.merge_sort(right)
        
        return Sort.merge(left_lst, right_lst)
    
    @staticmethod
    def merge(left_lst, right_lst):
        
        i = 0
        j = 0
        result = []
        
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                result.append(left_lst[i])
                i += 1
            else:
                result.append(right_lst[j])
                j += 1
                
        result.extend(left_lst[i:])
        result.extend(right_lst[j:])
        
        return result
    
    
    @staticmethod
    def quick_sort2(arr, left=0, right=-1):
        if right == -1:
            right = len(arr) -1
            
        if right > left:
            pivot_index = Sort.partition(arr, left, right)
            Sort.quick_sort2(arr, left, pivot_index-1)
            Sort.quick_sort2(arr, pivot_index+1, right)
            return arr
        
    @staticmethod
    def partition(arr, left, right):
        
        pivot = arr[right]
        pre_pivot = left -1
        
        for index in range(left, right):
            if arr[index] <= pivot:
                pre_pivot += 1
                arr[pre_pivot], arr[index] = arr[index], arr[pre_pivot]
                
        arr[pre_pivot+1], arr[right] = arr[right], arr[pre_pivot+1]
        return pre_pivot + 1
    
    @staticmethod
    def quick_sort(arr):
        
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        left = [i for i in arr if i < pivot]
        middle = [i for i in arr if i == pivot]
        right = [i for i in arr if i > pivot]
        
        return Sort.quick_sort(left) + middle + Sort.quick_sort(right)
    
    @staticmethod
    def insertion(arr):
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr




