# heaps will take an unsorted list and put them in a tree
# heap will send the largest number to the top and put them
# in a sorted list
# send the largest number to the top again and put it in the
# sorted list


def heapsort(arr):
    heap = Heap()
    # initializes sorted into an array full of 0 in the length
    # the array input
    sorted = [0 for _ in range(len(arr))]
    # THIS DOES THE SAME EXACT THING
    # sorted = [0] * len(arr)

    for el in arr:
        heap.insert(el)

    for i in range(len(arr)):
        sorted[len(arr) - i - 1] = heap.delete()
        #this will take the element from hea.delete
        #and put it into our sorted array in the last index
        #and will put elements in backwards so we dont have to
        #reverse our sorted array later
        #fancy

    return sorted


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        retval = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return retval

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            index = (index - 1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            mc = self._max_child(index)
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
            index = mc

    def _max_child(self, index):
        if index * 2 + 2 > len(self.storage) - 1:
            return index * 2 + 1
        else:
            return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
