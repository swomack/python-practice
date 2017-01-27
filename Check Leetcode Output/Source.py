

def check_list_output(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        
        index += 1
    
    return True



print(check_list_output(['bb', 'cc'], ['cc', 'bb']))

    