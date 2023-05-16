class List:
    def remove_(self, integer_list, values_list):
        values_list = list(dict.fromkeys(values_list))
        new_integer_list = integer_list.copy()
        for itemx in values_list:
            for itemy in integer_list:
                if itemy == itemx:
                    new_integer_list.remove(itemx)

        integer_list = new_integer_list.copy()
        print(values_list)
        return integer_list
    
    def remove_best(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]

obj = List()
print(obj.remove_([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3, 3]))