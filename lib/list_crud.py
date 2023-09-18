def create_an_empty_list():
    return []

def create_a_list():
    my_list = [1, 2, "apple", True]  # Example list with four elements
    return my_list
    
def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list

def add_element_to_start_of_list(my_list, element):
    my_list.insert(0, element)
    return my_list

def remove_element_from_end_of_list(my_list):
    if len(my_list) > 0:
        my_list.pop()
    return my_list

def remove_element_from_start_of_list(my_list):
     if len(my_list) > 0:
         del my_list[0]
         return my_list

def retrieve_first_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[0]
    else:
        return None  

def retrieve_element_from_index(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return None  

def retrieve_last_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[-1]
    else:
        return None