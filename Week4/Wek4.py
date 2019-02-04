import ctypes

class my_list:

    def __init__(self):
        self._number_of_items_in_list = 0
        self._capacity = 10
        self._storage = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return ( capacity * ctypes.py_object)()

    def __len__(self):
        return self._number_of_items_in_list

    def __getitem__(self, index):
        if not 0 <= index < self._number_of_items_in_list:
            raise IndexError("Invalid Index")
        return self._storage[index]

    def append(self, item):
        self._ensure_capacity_to_add()
        self._storage[self._number_of_items_in_list] = item
        self._number_of_items_in_list += 1

    def _resize(self, new_capacity):
        new_storage = self._make_array(new_capacity)
        for index in range(self._capacity):
            new_storage[index] = self._storage[index]
        self._storage = new_storage
        self._capacity = new_capacity

    def _ensure_capacity_to_add(self):
        if self._number_of_items_in_list == self._capacity:
            self._resize(self._capacity*2)

    def insert(self, index, value):
        self._ensure_capacity_to_add()
        for index_to_shift in range(self._number_of_items_in_list, index, -1):
            self._storage[index_to_shift] = self._storage[index_to_shift-1]
        self._storage[index] = value
        self._number_of_items_in_list += 1

    def remove(self, value):
        for index in range(0, self._number_of_items_in_list):
            if self._storage[index] == value:
                for index_to_shift in range(index, self._number_of_items_in_list - 1):
                    self._storage[index_to_shift] = self._storage[index_to_shift+1]
                self._storage[self._number_of_items_in_list-1] = None
                self._number_of_items_in_list -= 1
                return
        raise ValueError('value not found')




some_new_list = my_list()

for number in range(35):
    some_new_list.append(number)


some_new_list.insert(10, 100)

some_new_list.remove(0)

for index in range(len(some_new_list)):
    print(some_new_list[index])