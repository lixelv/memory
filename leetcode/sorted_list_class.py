class SortedList(list):
    def __init__(self, *args, sorted=False, key=lambda x: x):
        if sorted:
            super().__init__(*args)
            self.key = key
        else:
            super().__init__(*args)
            self.sort(key=key)
            self.key = key

    def index(self, value, return_anyway=False):
        left = 0
        right = len(self) - 1

        while left <= right:
            middle = (left + right) // 2
            if self.key(self[middle]) < self.key(value):
                left = middle + 1
            elif self.key(self[middle]) > self.key(value):
                right = middle - 1
            else:
                if middle > 0:
                    while self.key(self[middle - 1]) == self.key(value):
                        middle -= 1
                return middle

        return right if return_anyway else None

    def count(self, value):
        index = self.index(value)
        if index is None:
            return 0
        else:
            sub_index = index
            result = 1

            while sub_index < len(self) - 1:
                if self[sub_index + 1] == value:
                    sub_index += 1
                    result += 1
                else:
                    break

            sub_index = index

            while sub_index > 0:
                if self[sub_index - 1] == value:
                    sub_index -= 1
                    result += 1
                else:
                    break

            return result

    def append(self, value):
        index = self.index(value, return_anyway=True)
        self.insert(index + 1, value)
