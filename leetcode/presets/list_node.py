class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self._next = next
        self.size = None
        self.last = None

    @classmethod
    def from_iter(*args):
        cls = args[0]
        if (
            len(args) == 2
            and hasattr(args[1], "__iter__")
            and not isinstance(args[1], (str, bytes))
        ):
            iterator = iter(args[1])
        else:
            iterator = iter(args[1:])

        try:
            first_val = next(iterator)
        except StopIteration:
            return None

        node = cls(first_val)
        i = 1
        current = node

        for val in iterator:
            i += 1
            current._next = cls(val)
            current = current._next

        node.size = i
        node.last = current

        return node

    def __iter__(self):
        current = self

        while current is not None:
            yield current.val
            current = current._next

    def __len__(self):
        if self.size is None:
            result = 0
            current = self

            while current is not None:
                result += 1
                current = current._next

            self.size = result

        return self.size

    def __repr__(self):
        return "[" + " -> ".join([repr(i) for i in self]) + "]"

    def __getitem__(self, index):
        if isinstance(index, int):
            i = 0
            current = self

            if index < 0:
                index = len(self) - index

            while current is not None:
                if i == index:
                    return current.val

                i += 1
                current = current._next

            raise IndexError("Index out of range!")

        elif isinstance(index, slice):
            return self.__class__.from_iter(tuple(self)[slice])

    def copy(self):
        if self is None:
            return None

        new_list = ListNode(self.val)
        current_old = self._next
        current_new = new_list

        while current_old is not None:
            current_new._next = ListNode(current_old.val)
            current_old = current_old._next
            current_new = current_new._next

        return new_list

    def append(self, el):
        self.last._next = self.__class__(el)
        self.last = self.last._next
        self.size += 1


a = ListNode.from_iter([1, 2, 3, 4])
a.last._next = ListNode.from_iter(5, 6, 7)
a.append(5)
a.append(6)
a.append(7)

print(a)
