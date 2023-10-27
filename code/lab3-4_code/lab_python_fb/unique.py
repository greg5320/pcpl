from gen_random import gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = list(items)  
        self.index = 0
        self.unique_items = []

    def _get_key(self, item):
        if self.ignore_case and isinstance(item, str):
            return item.lower()
        return item

    def __next__(self):
        while self.index < len(self.items):
            current_item = self.items[self.index]
            key = self._get_key(current_item)
            if key not in self.unique_items:
                self.unique_items.append(key)
                self.index += 1
                return current_item
            else:
                self.index += 1
        raise StopIteration

    def __iter__(self):
        return self


data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for i in Unique(data):
    print(i)  
print()
data_random = gen_random(10,1,3)
for i in Unique(data_random):
    print(i)
print()
data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for i in Unique(data_str):
    print(i)  
print()
for i in Unique(data_str, ignore_case=True):
    print(i)  
