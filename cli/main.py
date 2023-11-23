from loader import Loader

personnel = Loader(model="personnel")
stock = Loader(model="stock")


class WarehouseController:
    
    def __init__(self, name:str) -> None:
        self.name = name

    def __employee_name_check(self, employee) -> bool:
        """
        Description:
            This private function checks if the 'name' instance attribute corresponds to a validated user.
        Args:
            employee (Employee): An instance of the Employee class to be validated
        Returns:
            bool: True if the user is validated, otherwise False.
        """
        if employee.user_name == self.name:
            return True

        for baby_employee in employee.head_of:
            if self.__employee_name_check(baby_employee):
                return True
        return False

    def factory_check(self, check:str) -> bool:
        """
        Description:
            This function performs one of two validations based on the provided argument. If 'name' is passed to the 'check' argument, 
            it verifies whether the 'self.name' instance attribute is registered. If 'password' is passed, it checks whether the 
            'self.name' and the provided password are validated against stored credentials.

        Args:
            check (str): Use 'name' to verify if 'self.name' is registered. Use 'password' to check if the provided password matches 
                        the one associated with 'self.name'.

        Returns:
            bool: True if the validation is successful, False otherwise.
        """
        if check == 'name':
            for user in personnel:
                if self.__employee_name_check(user):
                    return True
            return False

        if check == 'password':
            password = input('Enter the password: ')
            for user in personnel:
                if self.__log_in_check(user, password):
                    return True
            return False
        
    def __log_in_check(self, employee, password):
        """
        Description:
            This private function checks if the 'self.name' attribute and a provided password
            are validated against stored credentials for an Employee instance.

        Args:
            employee (Employee): An instance of the Employee class whose name and password are to be validated.
            password (str): The password to check against the 'self.name' credential.

        Returns:
            bool: True if the 'self.name' and password are validated, otherwise False.
        """
        
        if employee.user_name == self.name and employee.authenticate(password):
            return True
        
        for baby_employee in employee.head_of:
            if self.__log_in_check(baby_employee, password):
                return True
        return False
    
    @staticmethod
    def list_items_warehouse(house_number: int, items_per_pages: int = 50) -> None:
        """
        Description:
            This function displays the list of items according to warehouse ID by pagination.

        Args:
            house_number (int): The warehouse ID to be processed.
            items_per_pages (int, optional): The number of items to display on each page. Defaults to 50.

        Returns:
            None: It prints out the list of items
        """
        warehouse_id = f"{house_number}"

        for warehouse in stock:
            if warehouse.id == warehouse_id:
                total_items = len(warehouse.stock)
                start = 0
                item_count = 0
                while start * items_per_pages < total_items:
                    start_index = start * items_per_pages
                    end_index = start_index + items_per_pages
                    items_in_list = warehouse.stock[start_index:end_index]
                    for item in items_in_list:
                        item_count += 1
                        print(f"{item}")
                    print()
                    print(
                        f"Displayed {item_count} items out of {total_items} from warehouse {warehouse_id}"
                    )
                    prompt = input(
                        "Please press any key for next page or 'q' for quit: "
                    )
                    start += 1
                    if prompt == "q":
                        break



warehouse_1 = WarehouseController('Martha')

# warehouse_1.list_items_warehouse(3)


check = warehouse_1.factory_check('password')

print(check)


